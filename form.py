# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(100, 50, 450, 450))
        self.image.setObjectName("image")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 50, 115, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 80, 115, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(640, 270, 59, 16))
        self.label_2.setObjectName("label_2")
        self.res = QtWidgets.QLabel(self.centralwidget)
        self.res.setGeometry(QtCore.QRect(640, 300, 59, 16))
        self.res.setObjectName("res")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 110, 115, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.load_pic)
        self.pushButton_2.clicked.connect(MainWindow.first_segment)
        self.pushButton_3.clicked.connect(MainWindow.edge_detector)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "LoadPIc"))
        self.pushButton_2.setText(_translate("MainWindow", "FirstSegment"))
        self.label_2.setText(_translate("MainWindow", "res"))
        self.res.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_3.setText(_translate("MainWindow", "EdgeDetector"))

