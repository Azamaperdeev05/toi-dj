#pragma once

#include <QModelIndex>
#include <QObject>
#include <QUrl>
#include <QVariant>

#include "library/trackset/baseplaylistfeature.h"
#include "preferences/usersettings.h"
#include "util/parented_ptr.h"

class TreeItem;
class QPoint;

class PlaylistFeature : public BasePlaylistFeature {
    Q_OBJECT

  public:
    PlaylistFeature(
            Library* pLibrary,
            UserSettingsPointer pConfig);
    ~PlaylistFeature() override = default;

    QVariant title() override;

    bool dropAcceptChild(const QModelIndex& index,
            const QList<QUrl>& urls,
            QObject* pSource) override;
    bool dragMoveAcceptChild(const QModelIndex& index, const QList<QUrl>& urls) override;

    void switchToWeddingStage(int stage);

  public slots:
    void onRightClick(const QPoint& globalPos) override;
    void onRightClickChild(const QPoint& globalPos, const QModelIndex& index) override;

  private slots:
    void slotPlaylistTableChanged(int playlistId) override;
    void slotPlaylistContentOrLockChanged(const QSet<int>& playlistIds) override;
    void slotPlaylistTableRenamed(int playlistId, const QString& newName) override;
    void slotShufflePlaylist();
    void slotOrderTracksByCurrentPosition();
    void slotUnlockAllPlaylists();
    void slotDeleteAllUnlockedPlaylists();
    void slotToiStageChanged(double stageVal);
    void slotNewEventRequested(double val);

  protected:
    void decorateChild(TreeItem* pChild, int playlistId) override;
    QList<IdAndLabel> createPlaylistLabels();
    QModelIndex constructChildModel(int selectedId);

  private:
    void ensureDefaultWeddingPlaylists();
    QString getRootViewHtml() const override;

    parented_ptr<QAction> m_pShufflePlaylistAction;
    parented_ptr<QAction> m_pOrderByCurrentPosAction;
    parented_ptr<QAction> m_pUnlockPlaylistsAction;
    parented_ptr<QAction> m_pDeleteAllUnlockedPlaylistsAction;

    std::unique_ptr<ControlObject> m_pToiStageControl;
    std::unique_ptr<ControlProxy> m_pToiStageProxy;
    std::unique_ptr<ControlObject> m_pNewEventControl;
    std::unique_ptr<ControlProxy> m_pNewEventProxy;
};
