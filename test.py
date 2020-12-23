# -*- coding: utf-8 -*-

"""
Module implementing pq_result.
"""

from PySide2.QtCore import QSize, QThread, Signal, QObject, QFile, QIODevice
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QDesktopWidget
from PySide2.QtGui import QIcon, QPixmap, QGuiApplication
import sys, os

from shutil import copyfile
from time import sleep
from threading import Thread, Lock
from PySide2.QtUiTools import QUiLoader


class AVTResult():
    def __init__(self):
        self.ui = QUiLoader().load("avt_result.ui")
        self.actions()

    def actions(self):
        self.ui.btn_run.clicked.connect(self.test)
    
    def test(self):
        Test().test(self.ui)

class Test():
    def test(self, ui):
        ui.textBrowser_info.append("Test")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_win = AVTResult()

    # style_file = QFile(':/ui/style.qss')
    # style_file = QFile('style.qss')
    # style_file.open(QIODevice.ReadOnly)
    # my_win.ui.setStyleSheet(((style_file.readAll()).data()).decode())

    my_win.ui.show()
    sys.exit(app.exec_())