from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6 import uic
import Downloader
from gui import MainFramework as mf

# Only needed for access to command line arguments
import sys

app = QApplication(sys.argv)
window = mf.MainWindow()
window.show()
app.exec()
