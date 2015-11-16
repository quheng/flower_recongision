# -*- coding: utf-8 -*-

#convert ui file to python, then import it
import os
os.system('pyuic5 -o Form.py form.ui')
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import form
import re

class MainWindow(QMainWindow):
    """the main user interface"""
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = form.Ui_MainWindow()
        self.ui.setupUi(self)
        self.paramter = range(10)

    def load_dic(self):
        folder = QFileDialog.getExistingDirectory()
        self.paramter[0] = folder
        self.cm_load_dic()

    def test_single_pic(self):
        file = QFileDialog.getOpenFileName()# 返回的是一个tuple
        self.ui.image.setPixmap(QPixmap(file[0]))
        self.paramter[0] = file[0]
        self.cm_test_single_pic()
        self.ui.res.setText(self.res[0])
