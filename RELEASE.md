# TOI DJ (MVP 1.0.0) — Release Notes & Documentation

**TOI DJ** — қазақ тойларына арналған мамандандырылған, заманауи және ыңғайлы DJ бағдарламасы (A specialized, standalone DJ workstation crafted specifically for Kazakh wedding ceremonies and events).

---

## 1. Description & Overview

TOI DJ combines the audio engine reliability of open-source DJ software with a tailored interface designed specifically for live wedding hosts and DJs (той диджейлері):
- **12 Wedding Ceremony Stages (Той режимдері)**: Instant access to tailored stages from guest arrival to the grand finale.
- **Dedicated Ceremony Actions**: One-click **ЖАҢА ТОЙ** (New Event reset) that safely clears active queue/requests while protecting music library, user playlists, favorites, and history.
- **Kazakh & Bilingual Interface**: Fully localized terminology, streamlined 2-deck layout, integrated Kazakh queue (**КЕЗЕК**), and search.
- **Zero-Latency Audio**: Native Apple CoreAudio integration with hardware-accelerated processing.

---

## 2. Supported Platform & System Requirements

- **Operating System**: macOS 12 (Monterey), macOS 13 (Ventura), macOS 14 (Sonoma), macOS 15 (Sequoia), or later.
- **Hardware Architecture**: **Apple Silicon (M1 / M2 / M3 / M4 and Pro/Max/Ultra variants) — `arm64`**.
- **Display Resolution**: Tested and optimized for 1280×668, 1440×900, 1680×1050, 1920×1080 and Retina displays.
- **Audio Output**: Built-in MacBook speakers, 3.5mm headphone jack, USB DJ controllers, and external USB/Thunderbolt CoreAudio sound cards.

---

## 3. Installation Instructions

You can install TOI DJ using either the Disk Image (`.dmg`) or the portable archive (`.zip`):

### Option A: Via DMG (Recommended)
1. Double-click `TOI-DJ-MVP-1.0.0-macOS-arm64.dmg` (or `TOI-DJ-macOS-arm64.dmg`).
2. Drag **TOI DJ.app** into the **Applications** folder shortcut.
3. Eject the DMG disk image.

### Option B: Via ZIP
1. Unzip `TOI-DJ-MVP-1.0.0-macOS-arm64.zip`.
2. Move **TOI DJ.app** to your `/Applications` directory.

---

## 4. First Launch Instructions (Gatekeeper / Permissions)

Because this is a locally built release without an Apple Developer ID notarization certificate:
1. Double-click **TOI DJ.app** in Applications.
2. If macOS displays a notice that the developer cannot be verified:
   - Open **System Settings** → **Privacy & Security** (Жүйелік баптаулар → Құпиялық және қауіпсіздік).
   - Scroll down to the **Security** section.
   - Click **Open Anyway** (Бәрібір ашу) next to `TOI DJ.app`.
   - Alternatively, right-click (or Control-click) `TOI DJ.app` and choose **Open**.
3. When prompted, grant Microphone/Audio access if you plan to use microphone input.

---

## 5. Adding Music to Library

1. Launch **TOI DJ**.
2. Go to top menu: **Файл (File)** → **Медиатека қалтасын таңдау... (Choose Music Directory...)**.
3. Select your music collection folder (e.g. `~/Music` or your external USB drive).
4. The scanner will automatically index tracks, calculate BPM, detect keys, and populate **Музыка кітапханасы**.
5. Use the instant search bar (press `/` or click search) to find any song by artist or title.

---

## 6. Configuring Audio Devices

1. Click **БАПТАУЛАР** (Settings) in the top-right toolbar (or press `Cmd + ,`).
2. In the **Дыбыстық жабдық (Sound Hardware)** tab:
   - **Master Output**: Select `Динамики MacBook` (Built-in speakers) or your external sound card / DJ controller.
   - **Headphones (Құлаққап)**: Choose your cue channel for pre-listening.
3. Click **Қолдану (Apply)** and **OK**.

---

## 7. Basic Keyboard Shortcuts

| Shortcut | Action | Описание |
| :--- | :--- | :--- |
| `Alt + Left` | Load Track to Deck A | Таңдалған әнді А декасына жүктеу |
| `Alt + Right` | Load Track to Deck B | Таңдалған әнді В декасына жүктеу |
| `D` | Play / Pause Deck A | Дека А: Ойнату / Кідірту |
| `C` | Cue Deck A | Дека А: CUE нүктесі |
| `L` | Play / Pause Deck B | Дека В: Ойнату / Кідірту |
| `K` | Cue Deck B | Дека В: CUE нүктесі |
| `Shift + Up / Down` | Crossfader nudge Left / Right | Кроссфейдерді жылжыту |
| `Alt + 1` .. `Alt + =` | Switch Wedding Stages 1 to 12 | Той режимдерін ауыстыру |
| `Space` | Maximize / Restore Library | Кітапхананы толық экранға ашу |
| `Cmd + F` | Search Music Library | Кітапханадан іздеу |
| `Cmd + ,` | Preferences / Settings | Баптаулар терезесін ашу |

---

## 8. The 12 Wedding Stages (12 Той режимдері)

The top toolbar features direct access to all 12 canonical Kazakh wedding stages:

1. **1. ҚОНАҚТАРДЫ КҮТУ** (`Alt + 1`): Welcome background lounge music while guests gather.
2. **2. ЖҰПТЫҢ КІРУІ** (`Alt + 2`): Grand entrance of the newlyweds / ceremonial fanfare.
3. **3. БЕТАШАР** (`Alt + 3`): Traditional face-revealing ceremony and dombyra accompaniment.
4. **4. АҚ ТІЛЕК / ТОСТАР** (`Alt + 4`): Warm acoustic background for elder blessings and speeches.
5. **5. ТОЙ БАС ТАБАҚ** (`Alt + 5`): Traditional dinner banquet ambiance.
6. **6. ЖАСТАР БИІ** (`Alt + 6`): Romantic first slow dance of the bride and groom.
7. **7. ДИНАМИКАЛЫҚ БИЛЕР** (`Alt + 7`): High-energy peak party dance hits (қазақша, шет елдік).
8. **8. ҚЫЗЫҚТЫ ОЙЫНДАР** (`Alt + 8`): Playful interactive competition music and game stingers.
9. **9. КЕЛІН ТҮСІРУ / САЛТ** (`Alt + 9`): Deeply traditional ritual ceremonies.
10. **10. ТОЙ ТОРТЫ** (`Alt + 0`): Triumphant celebration music for the wedding cake cutting.
11. **11. БУКЕТ / ГҮЛ ТАСТАУ** (`Alt + -`): Dynamic bridal bouquet and garter toss excitement.
12. **12. ТОЙДЫ ҚОРЫТЫНДЫЛАУ** (`Alt + =`): Emotional farewell gratitude song and guest sendoff.

*Note: Switching wedding stages never interrupts running playback or active playlists.*

---

## 9. Technology Foundation & Credits

- Built upon the robust, real-time C++ audio engine and architecture of **Mixxx** (v2.7 development line).
- Tailored and packaged by the TOI DJ development team for wedding and event professionals.
- Mixxx is open-source software licensed under GPLv2+. All original Mixxx source code and licenses are preserved in the codebase.

---

## 10. Development Build Information

- **Branch**: `toi-dj`
- **Architecture**: `arm64` (Apple Silicon)
- **Compiler**: AppleClang 17.0.0
- **Build Type**: `Release` (optimized with `-O3`, `-funroll-loops`, `-ffast-math`)
- **Release Version**: `TOI DJ MVP 1.0.0` (Internal base: `2.7.0-alpha`)
- **Packaged Artifacts**:
  - `dist/TOI DJ.app` (Self-contained macOS Application Bundle)
  - `dist/TOI-DJ-MVP-1.0.0-macOS-arm64.dmg` (Installer Disk Image)
  - `dist/TOI-DJ-MVP-1.0.0-macOS-arm64.zip` (Portable ZIP archive)

---

## 11. Known Limitations

1. **Architecture**: This release is compiled specifically for Apple Silicon (M1/M2/M3/M4). It does not natively run on legacy Intel x86_64 Macs without recompilation.
2. **First Launch Gatekeeper**: Because the local build is signed with an ad-hoc certificate (`codesign -s -`), macOS Gatekeeper requires the standard one-time right-click → "Open" confirmation on initial execution.
3. **JACK Audio**: JACK audio client library is not bundled as macOS native CoreAudio is the primary and recommended high-performance audio engine.
