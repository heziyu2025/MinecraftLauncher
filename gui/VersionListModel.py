from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt

tick = QtGui.QImage('tick.png')

class VersionListModel(QtCore.QAbstractListModel):
    def __init__(self, *args, versions=None, **kwargs):
        super(VersionListModel, self).__init__(*args, **kwargs)
        self.versions = versions or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            id, type, releaseTime = self.versions[index.row()]
            return id#, type, releaseTime

        if role == Qt.ItemDataRole.DecorationRole:
            id, type, releaseTime = self.versions[index.row()]
            if id:
                return id#, type, releaseTime

    def rowCount(self, index):
        return len(self.versions)