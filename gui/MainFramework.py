from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6 import uic
from . import VersionListModel as vl
import Downloader
import json

# Only needed for access to command line arguments
import sys

# load UI
ui_file = "gui/mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(ui_file)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)                
        Ui_MainWindow.__init__(self)
        self.setupUi(self) 

        # create a layout for central widget
        self.centralLayout = QVBoxLayout()
        self.centralwidget.setLayout(self.centralLayout)

        # # Connect the button.
        # self.addButton.pressed.connect(self.add)
        # self.deleteButton.pressed.connect(self.delete)
        # self.completeButton.pressed.connect(self.complete)       
        
        self.currVerLayout = QHBoxLayout()
        self.currVerLayout.addWidget(QLabel("Current Version: "))
        self.lblCurrVer = QLabel("1.2.1.1")
        self.currVerLayout.addWidget(self.lblCurrVer)
        self.centralLayout.addLayout(self.currVerLayout)    
        
        self.otherVerLayout = QHBoxLayout()
        self.otherVerLayout.addWidget(QLabel("Other Versions: "))
        self.btnOtherVer = QPushButton("Load other versions")
        self.btnOtherVer.pressed.connect(self.fetchVers)     
        self.otherVerLayout.addWidget(self.btnOtherVer)
        self.centralLayout.addLayout(self.otherVerLayout)

        self.verListView = QListView()
        self.centralLayout.addWidget(self.verListView)

        # get version data
        versions = Downloader.get_version_list()
        ver_release = []
        ver_others = []
        for v in versions["versions"]:
            var={v["id"], v["type"], v["releaseTime"]}
            if v["type"] == "release":
                ver_release.append(var)
            else:
                ver_others.append(var)
                
        #self.load()
        self.model = vl.VersionListModel(versions=ver_release)
        self.verListView.setModel(self.model)

    def add(self):
        """
        Add an item to our todo list, getting the text from the QLineEdit .todoEdit
        and then clearing it.
        """
        text = self.todoEdit.text()
        if text: # Don't add empty strings.
            # Access the list via the model.
            self.model.versions.append((False, text))
            # Trigger refresh.
            self.model.layoutChanged.emit()
            # Empty the input
            self.todoEdit.setText("")
            self.save()

    def delete(self):
        indexes = self.verListView.selectedIndexes()
        if indexes:
            # Indexes is a list of a single item in single-select mode.
            index = indexes[0]
            # Remove the item and refresh.
            del self.model.versions[index.row()]
            self.model.layoutChanged.emit()
            # Clear the selection (as it is no longer valid).
            self.verListView.clearSelection()
            self.save()

    def complete(self):
        indexes = self.verListView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.versions[row]
            self.model.versions[row] = (True, text)
            # .dataChanged takes top-left and bottom right, which are equal
            # for a single selection.
            self.model.dataChanged.emit(index, index)
            # Clear the selection (as it is no longer valid).
            self.verListView.clearSelection()
            self.save()

    def fetchVers(self):
        try:
            with open('data.db', 'r') as f:
                self.model.versions = json.load(f)
        except Exception:
            pass

    def load(self):
        try:
            with open('data.db', 'r') as f:
                self.model.versions = json.load(f)
        except Exception:
            pass

    def save(self):
        with open('data.db', 'w') as f:
            data = json.dump(self.model.versions, f)
