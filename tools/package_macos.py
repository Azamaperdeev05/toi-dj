#!/usr/bin/env python3
"""
Packaging script to produce a standalone TOI DJ macOS Application Bundle (.app)
and distributable DMG and ZIP release artifacts for Apple Silicon (arm64).
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

def run_cmd(cmd, cwd=None):
    print(f"-> Running: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    res = subprocess.run(cmd, cwd=cwd, shell=isinstance(cmd, str), capture_output=True, text=True)
    if res.returncode != 0:
        print(f"ERROR ({res.returncode}): {res.stderr}")
        sys.exit(res.returncode)
    return res.stdout.strip()

def main():
    repo_root = Path(__file__).resolve().parent.parent
    build_mixxx = repo_root / "build" / "mixxx"
    if not build_mixxx.exists():
        print(f"Error: {build_mixxx} not found. Please build the application first.")
        sys.exit(1)

    dist_dir = repo_root / "dist"
    app_dir = dist_dir / "TOI DJ.app"
    contents_dir = app_dir / "Contents"
    macos_dir = contents_dir / "MacOS"
    frameworks_dir = contents_dir / "Frameworks"
    resources_dir = contents_dir / "Resources"

    print("Cleaning previous dist artifacts...")
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir(parents=True, exist_ok=True)
    macos_dir.mkdir(parents=True, exist_ok=True)
    frameworks_dir.mkdir(parents=True, exist_ok=True)
    resources_dir.mkdir(parents=True, exist_ok=True)

    print("1. Copying executable...")
    target_bin = macos_dir / "TOI DJ"
    shutil.copy2(build_mixxx, target_bin)
    target_bin.chmod(0o755)

    print("2. Packaging Frameworks (libfdk-aac)...")
    deps_dir = repo_root / "buildenv" / "mixxx-deps-2.7-arm64-osx-1c20f84a" / "installed" / "arm64-osx-min1100" / "debug" / "lib"
    fdk_dylib = deps_dir / "libfdk-aac.2.0.3.dylib"
    if fdk_dylib.exists():
        target_fdk = frameworks_dir / "libfdk-aac.2.0.3.dylib"
        shutil.copy2(fdk_dylib, target_fdk)
        target_fdk.chmod(0o755)
        # Create symlinks
        symlink_2 = frameworks_dir / "libfdk-aac.2.dylib"
        if symlink_2.exists(): symlink_2.unlink()
        symlink_2.symlink_to("libfdk-aac.2.0.3.dylib")
        symlink_base = frameworks_dir / "libfdk-aac.dylib"
        if symlink_base.exists(): symlink_base.unlink()
        symlink_base.symlink_to("libfdk-aac.2.0.3.dylib")

    print("3. Updating rpaths on executable...")
    otool_out = run_cmd(["otool", "-l", str(target_bin)])
    lines = otool_out.splitlines()
    for i, line in enumerate(lines):
        if "cmd LC_RPATH" in line and i + 2 < len(lines):
            path_line = lines[i + 2].strip()
            if path_line.startswith("path "):
                old_rpath = path_line.split()[1]
                run_cmd(["install_name_tool", "-delete_rpath", old_rpath, str(target_bin)])

    run_cmd(["install_name_tool", "-add_rpath", "@executable_path/../Frameworks", str(target_bin)])

    print("4. Copying Resources...")
    res_root = repo_root / "res"
    resource_folders = ["skins", "keyboard", "controllers", "translations", "fonts", "effects", "images"]
    for folder in resource_folders:
        src = res_root / folder
        if src.exists():
            dst = resources_dir / folder
            print(f"   Copying {folder}...")
            shutil.copytree(src, dst)

    if (res_root / "schema.xml").exists():
        shutil.copy2(res_root / "schema.xml", resources_dir / "schema.xml")

    # Application icon
    icns_src = res_root / "osx" / "application.icns"
    if icns_src.exists():
        shutil.copy2(icns_src, resources_dir / "application.icns")

    print("5. Writing Info.plist and PkgInfo...")
    info_plist_content = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>TOI DJ</string>
    <key>CFBundleIconFile</key>
    <string>application.icns</string>
    <key>CFBundleIdentifier</key>
    <string>kz.toidj.toidj</string>
    <key>CFBundleName</key>
    <string>TOI DJ</string>
    <key>CFBundleDisplayName</key>
    <string>TOI DJ</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleSignature</key>
    <string>????</string>
    <key>CFBundleShortVersionString</key>
    <string>1.1.0</string>
    <key>CFBundleVersion</key>
    <string>1.1.0</string>
    <key>NSHumanReadableCopyright</key>
    <string>Copyright © 2026 TOI DJ Team</string>
    <key>NSMicrophoneUsageDescription</key>
    <string>TOI DJ requires microphone access for audio input.</string>
    <key>NSPrincipalClass</key>
    <string>NSApplication</string>
    <key>NSHighResolutionCapable</key>
    <true/>
    <key>LSApplicationCategoryType</key>
    <string>public.app-category.music</string>
    <key>LSMinimumSystemVersion</key>
    <string>11.0</string>
</dict>
</plist>
"""
    with open(contents_dir / "Info.plist", "w", encoding="utf-8") as f:
        f.write(info_plist_content)

    with open(contents_dir / "PkgInfo", "wb") as f:
        f.write(b"APPL????")

    print("6. Codesigning bundle (ad-hoc for Apple Silicon)...")
    run_cmd(["codesign", "--force", "--deep", "--sign", "-", str(app_dir)])
    run_cmd(["codesign", "--verify", "--deep", "--strict", str(app_dir)])

    print("7. Creating staging area for DMG...")
    dmg_staging = dist_dir / "dmg_staging"
    dmg_staging.mkdir(parents=True, exist_ok=True)
    # Copy app bundle into staging
    run_cmd(f'cp -R "{app_dir}" "{dmg_staging}/"', cwd=str(repo_root))
    # Create Applications link
    apps_link = dmg_staging / "Applications"
    if apps_link.exists() or apps_link.is_symlink():
        apps_link.unlink()
    apps_link.symlink_to("/Applications")

    dmg_path = dist_dir / "TOI-DJ-1.1.0-macOS-arm64.dmg"
    print(f"8. Building DMG: {dmg_path.name}...")
    run_cmd([
        "hdiutil", "create",
        "-volname", "TOI DJ",
        "-srcfolder", str(dmg_staging),
        "-ov",
        "-format", "UDZO",
        str(dmg_path)
    ])
    shutil.rmtree(dmg_staging)

    zip_path = dist_dir / "TOI-DJ-1.1.0-macOS-arm64.zip"
    print(f"9. Building ZIP: {zip_path.name}...")
    run_cmd(f'cd "{dist_dir}" && zip -r -y "{zip_path.name}" "TOI DJ.app"', cwd=str(repo_root))

    print("\n==========================================")
    print("TOI DJ PACKAGING COMPLETED SUCCESSFULLY!")
    print(f"Bundle: {app_dir}")
    print(f"DMG:    {dmg_path}")
    print(f"ZIP:    {zip_path}")
    print("==========================================")

if __name__ == "__main__":
    main()
