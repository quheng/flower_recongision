# -*- coding: utf-8 -*-

#convert ui file to python, then import it
import os
os.system('pyuic5 -o Form.py form.ui')
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import form
import re
import segment
import numpy
import cv2

class MainWindow(QMainWindow):
    """the main user interface
        numImage:  ndarray the current image
        qImage: QPixmap
    """

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = form.Ui_MainWindow()
        self.ui.setupUi(self)

    def load_pic(self):
        file = QFileDialog.getOpenFileName()# 返回的是一个tuple
        if (file != None):
            self.qImage = QPixmap(file[0])
            self.__show_img(self.qImage)
            self.numImage = cv2.imread(file[0])
    def first_segment(self):
        try:
            self.numImage, self.mask = segment.grab_cut(self.numImage)
        except Exception as e:
            print e.message
            reply = QMessageBox.information(self,"Error","please open an image first!",QMessageBox.Ok)

    def edge_detector(self):
        try:
            segment.edge_detec(self.mask)
        except Exception as e:
            print e.message
            reply = QMessageBox.information(self,"Error","please segment first!",QMessageBox.Ok)

    def test_single_pic(self):
        file = QFileDialog.getOpenFileName()# 返回的是一个tuple
        self.ui.image.setPixmap(QPixmap(file[0]))
        self.paramter[0] = file[0]
        self.cm_test_single_pic()
        self.ui.res.setText(self.res[0])

    def __show_img(self, picture):
        picture = picture.scaled(450,450,Qt.KeepAspectRatio)
        self.ui.image.setPixmap(picture)

