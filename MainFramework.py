from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QListView, QGridLayout, QLabel
import download

# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

versionGridLayout = QGridLayout()
versionGridLayout.setContentsMargins(1,1,1,1)

head1=QLabel()
head1.setText("release time")
head2=QLabel()
head2.setText("version")
versionGridLayout.addWidget(head1, 0, 0)
versionGridLayout.addWidget(head2, 0, 1)
versions = download.get_version_list()
idx=1
for v in versions["versions"]:
    btn = QPushButton()
    btn.setText(v["id"])
    ver=QLabel()
    ver.setText(v["releaseTime"])
    versionGridLayout.addWidget(ver, idx, 0)
    versionGridLayout.addWidget(btn, idx, 1)
    idx+=1


# Create a Qt widget, which will be our window.
window = QWidget()
window.setLayout(versionGridLayout)
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.
