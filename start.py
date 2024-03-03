import sys
from PyQt6.QtWidgets import *
from gui import MainFramework as mf

app = QApplication(sys.argv)
window = mf.MainWindow()
window.show()
app.exec()
