#coding=utf8
"""
# Author: quheng
# Created Time : Sun Sep  6 20:28:44 2015
"""
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import os
from window import MainWindow

if __name__ == '__main__':
    import sys
    application = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(application.exec_())
