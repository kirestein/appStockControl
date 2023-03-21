# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(833, 540)
        Login.setStyleSheet(u"background-color: rgb(0, 33, 99) ")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(149, 119, 561, 341))
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.2)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(170, 260, 181, 28))
        font = QFont()
        font.setPointSize(12)
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(122, 60, 291, 171))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.txt_user = QLineEdit(self.widget)
        self.txt_user.setObjectName(u"txt_user")
        font1 = QFont()
        font1.setPointSize(11)
        self.txt_user.setFont(font1)
        self.txt_user.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_user.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_user)

        self.txt_password = QLineEdit(self.widget)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setFont(font1)
        self.txt_password.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_password)

        self.label_3 = QLabel(Login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 10, 131, 131))
        self.label_3.setPixmap(QPixmap(u"../curso_Qt_creator/Nova pasta/assets/icon.png"))
        self.label_3.setScaledContents(True)
        self.label_3.raise_()
        self.frame.raise_()

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"Login", None))
        self.txt_user.setPlaceholderText(QCoreApplication.translate("Login", u"User", None))
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Login", u"Password", None))
        self.label_3.setText("")
    # retranslateUi

