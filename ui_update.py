# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_update.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(504, 166)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/download.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-image: url(:/newPrefix/img/background.jpg);")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(50, 100, 401, 20))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setStyleSheet("font: 11pt \"宋体\";")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.progressBar.setObjectName("progressBar")
        self.label_cont = QtWidgets.QLabel(Form)
        self.label_cont.setGeometry(QtCore.QRect(330, 70, 121, 16))
        self.label_cont.setAutoFillBackground(False)
        self.label_cont.setStyleSheet("font: 11pt \"宋体\";")
        self.label_cont.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_cont.setObjectName("label_cont")
        self.label_speed = QtWidgets.QLabel(Form)
        self.label_speed.setGeometry(QtCore.QRect(70, 70, 221, 16))
        self.label_speed.setAutoFillBackground(False)
        self.label_speed.setStyleSheet("font: 11pt \"宋体\";")
        self.label_speed.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_speed.setObjectName("label_speed")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 251, 16))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("font: 11pt \"宋体\";")
        self.label.setObjectName("label")
        self.pushButton_close = QtWidgets.QPushButton(Form)
        self.pushButton_close.setGeometry(QtCore.QRect(480, 5, 18, 18))
        self.pushButton_close.setStyleSheet("QPushButton{background: transparent;}\n"
"QPushButton{image: url(:/newPrefix/img/关闭.png);}\n"
"QPushButton:hover{image: url(:/newPrefix/img/关闭A.png);}\n"
"QPushButton:pressed{image: url(:/newPrefix/img/关闭A.png);}")
        self.pushButton_close.setText("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_remove = QtWidgets.QPushButton(Form)
        self.pushButton_remove.setGeometry(QtCore.QRect(460, 5, 18, 18))
        self.pushButton_remove.setStyleSheet("QPushButton{background: transparent;}\n"
"QPushButton{image: url(:/newPrefix/img/最小化.png);}\n"
"QPushButton:hover{image: url(:/newPrefix/img/最小化A.png);}\n"
"QPushButton:pressed{image: url(:/newPrefix/img/最小化A.png);}")
        self.pushButton_remove.setText("")
        self.pushButton_remove.setObjectName("pushButton_remove")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "update"))
        self.progressBar.setFormat(_translate("Form", "当前进度：%p%"))
        self.label_cont.setText(_translate("Form", "更新包：0/0"))
        self.label_speed.setText(_translate("Form", "0 KB/s  0MB"))
        self.label.setText(_translate("Form", "冰山挖词  版本更新中..."))
import image_rc
