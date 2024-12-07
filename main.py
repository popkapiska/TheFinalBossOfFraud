from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
import urllib.request
from os import getcwd
import sys
from threading import Thread
url = "https://github.com/popkapiska/testtesttest/raw/refs/heads/main/rhythm-lab.com_amen_vol.1.zip"







Form, Window = uic.loadUiType("updater.ui")

class MainWindow(QtWidgets.QMainWindow,Form):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.progressBar.setValue(50)
        self.pushButton.clicked.connect(self.thestuff)



    def setprogress(self, count, blockSize, totalSize):
        percent = int(count * blockSize * 100 / totalSize)
        self.progressBar.setValue(percent)
    def thestuff(self):
        resp = urllib.request.urlretrieve(url, "sexxxxx.zip", reporthook=self.setprogress)


import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())