# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_control.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1136, 816)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 35))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_import = QPushButton(self.frame)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setMinimumSize(QSize(0, 35))
        self.btn_import.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_import)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setMinimumSize(QSize(0, 35))
        self.btn_tables.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 35))
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setMinimumSize(QSize(0, 35))
        self.btn_contato.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_contato)


        self.verticalLayout_2.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(0, 85, 0);")
        self.pg_tables = QWidget()
        self.pg_tables.setObjectName(u"pg_tables")
        self.verticalLayout_8 = QVBoxLayout(self.pg_tables)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.pg_tables)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout_7 = QVBoxLayout(self.tables)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.tw_estoque = QTreeWidget(self.tables)
        self.tw_estoque.setObjectName(u"tw_estoque")

        self.verticalLayout_5.addWidget(self.tw_estoque)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.tables)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.tw_saida = QTreeWidget(self.tables)
        self.tw_saida.setObjectName(u"tw_saida")

        self.verticalLayout_4.addWidget(self.tw_saida)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.frame_2 = QFrame(self.tables)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_gerar = QPushButton(self.frame_2)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setMinimumSize(QSize(100, 27))
        self.btn_gerar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 10);\n"
"	border-radius: 5px;\n"
"	font-size: 16px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	color: black;\n"
"	background-color: rgb(165, 255, 210);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_gerar)

        self.btn_estornar = QPushButton(self.frame_2)
        self.btn_estornar.setObjectName(u"btn_estornar")
        self.btn_estornar.setMinimumSize(QSize(100, 27))
        self.btn_estornar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 10);\n"
"	border-radius: 5px;\n"
"	font-size: 16px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	color: black;\n"
"	background-color: rgb(165, 255, 210);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_estornar)

        self.btn_importar = QPushButton(self.frame_2)
        self.btn_importar.setObjectName(u"btn_importar")
        self.btn_importar.setMinimumSize(QSize(100, 27))
        self.btn_importar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 10);\n"
"	border-radius: 5px;\n"
"	font-size: 16px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	color: black;\n"
"	background-color: rgb(165, 255, 210);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_importar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_10 = QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_10.addWidget(self.label_10)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_grafico = QPushButton(self.tab_2)
        self.btn_grafico.setObjectName(u"btn_grafico")
        self.btn_grafico.setMinimumSize(QSize(150, 35))
        self.btn_grafico.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 10);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	color: black;\n"
"	background-color: rgb(165, 255, 210);\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_grafico)

        self.btn_excel = QPushButton(self.tab_2)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(150, 35))
        self.btn_excel.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 10);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	color: black;\n"
"	background-color: rgb(165, 255, 210);\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_excel)


        self.verticalLayout_10.addLayout(self.horizontalLayout_13)

        self.txt_filtro = QLineEdit(self.tab_2)
        self.txt_filtro.setObjectName(u"txt_filtro")
        self.txt_filtro.setMinimumSize(QSize(0, 35))
        self.txt_filtro.setStyleSheet(u"color: rgba(211, 239, 241, 1);\n"
"border-bottom: 1px solid #fff;\n"
"border-radius: None;\n"
"background-color: rgba(86, 155, 102, 0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size: 21px;")
        self.txt_filtro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.txt_filtro)

        self.tb_stock = QTableView(self.tab_2)
        self.tb_stock.setObjectName(u"tb_stock")

        self.verticalLayout_10.addWidget(self.tb_stock)

        self.tabWidget.addTab(self.tab_2, "")
        self.label_10.raise_()
        self.btn_grafico.raise_()
        self.btn_excel.raise_()
        self.txt_filtro.raise_()
        self.tb_stock.raise_()

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.pg_tables)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.verticalLayout_12 = QVBoxLayout(self.pg_contato)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_7 = QLabel(self.pg_contato)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_12.addWidget(self.label_7)

        self.label_16 = QLabel(self.pg_contato)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_12.addWidget(self.label_16)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_17 = QLabel(self.pg_contato)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_2.addWidget(self.label_17)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_19 = QLabel(self.pg_contato)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_14.addWidget(self.label_19)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.stackedWidget.addWidget(self.pg_contato)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_11 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_8 = QLabel(self.pg_sobre)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 50))
        self.label_8.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_11.addWidget(self.label_8)

        self.label_15 = QLabel(self.pg_sobre)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_15.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_15)

        self.stackedWidget.addWidget(self.pg_sobre)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout = QVBoxLayout(self.pg_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.9);\n"
"border-radius: 15px;")

        self.verticalLayout.addWidget(self.label)

        self.btn_cadastro = QPushButton(self.pg_home)
        self.btn_cadastro.setObjectName(u"btn_cadastro")
        self.btn_cadastro.setMinimumSize(QSize(0, 30))
        self.btn_cadastro.setMaximumSize(QSize(16777215, 16777215))
        self.btn_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastro.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 10);\n"
"	border-radius: 5px;\n"
"	font-size: 16px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	color: black;\n"
"	background-color: rgb(165, 255, 210);\n"
"}")

        self.verticalLayout.addWidget(self.btn_cadastro)

        self.stackedWidget.addWidget(self.pg_home)
        self.pg_import = QWidget()
        self.pg_import.setObjectName(u"pg_import")
        self.label_4 = QLabel(self.pg_import)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 40, 1111, 81))
        self.widget = QWidget(self.pg_import)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 220, 1111, 111))
        self.horizontalLayout_11 = QHBoxLayout(self.widget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 35))
        font = QFont()
        font.setFamily(u"Trebuchet MS")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"color: rgba(211, 239, 241, 1);\n"
"border-bottom: 1px solid #fff;\n"
"border-radius: None;\n"
"background-color: rgba(86, 155, 102, 0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size: 21px;")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.lineEdit)

        self.btn_open_2 = QPushButton(self.widget)
        self.btn_open_2.setObjectName(u"btn_open_2")
        self.btn_open_2.setMinimumSize(QSize(75, 35))
        self.btn_open_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 10);\n"
"	border-top-right-radius: 15px;\n"
"	font-size: 16px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	color: black;\n"
"	background-color: rgb(165, 255, 210);\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_open_2)

        self.widget1 = QWidget(self.pg_import)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 460, 1111, 191))
        self.horizontalLayout_12 = QHBoxLayout(self.widget1)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_12.addWidget(self.label_5)

        self.btn_import_xml = QPushButton(self.widget1)
        self.btn_import_xml.setObjectName(u"btn_import_xml")
        self.btn_import_xml.setMinimumSize(QSize(250, 35))
        self.btn_import_xml.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_import_xml.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 10);\n"
"	border-radius: 5px;\n"
"	font-size: 16px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	color: black;\n"
"	background-color: rgb(165, 255, 210);\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_import_xml)

        self.label_9 = QLabel(self.widget1)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_12.addWidget(self.label_9)

        self.stackedWidget.addWidget(self.pg_import)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_9 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_14 = QLabel(self.pg_cadastro)
        self.label_14.setObjectName(u"label_14")
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_14)

        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.nome = QLabel(self.pg_cadastro)
        self.nome.setObjectName(u"nome")

        self.horizontalLayout_5.addWidget(self.nome)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setStyleSheet(u"color: rgba(211, 239, 241, 1);\n"
"border-bottom: 1px solid #fff;\n"
"border-radius: None;\n"
"background-color: rgba(86, 155, 102, 0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size: 21px;")

        self.horizontalLayout_5.addWidget(self.txt_nome)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.usuario = QLabel(self.pg_cadastro)
        self.usuario.setObjectName(u"usuario")

        self.horizontalLayout_6.addWidget(self.usuario)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setStyleSheet(u"color: rgba(211, 239, 241, 1);\n"
"border-bottom: 1px solid #fff;\n"
"border-radius: None;\n"
"background-color: rgba(86, 155, 102, 0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size: 21px;")

        self.horizontalLayout_6.addWidget(self.txt_usuario)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.senha = QLabel(self.pg_cadastro)
        self.senha.setObjectName(u"senha")

        self.horizontalLayout_7.addWidget(self.senha)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"color: rgba(211, 239, 241, 1);\n"
"border-bottom: 1px solid #fff;\n"
"border-radius: None;\n"
"background-color: rgba(86, 155, 102, 0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size: 21px;")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.txt_senha)

        self.btn_senha = QPushButton(self.pg_cadastro)
        self.btn_senha.setObjectName(u"btn_senha")
        self.btn_senha.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(170, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_senha)

        self.n_senha = QPushButton(self.pg_cadastro)
        self.n_senha.setObjectName(u"n_senha")
        self.n_senha.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(170, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_7.addWidget(self.n_senha)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.senha_2 = QLabel(self.pg_cadastro)
        self.senha_2.setObjectName(u"senha_2")

        self.horizontalLayout_8.addWidget(self.senha_2)

        self.txt_senha_2 = QLineEdit(self.pg_cadastro)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        self.txt_senha_2.setStyleSheet(u"color: rgba(211, 239, 241, 1);\n"
"border-bottom: 1px solid #fff;\n"
"border-radius: None;\n"
"background-color: rgba(86, 155, 102, 0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size: 21px;")
        self.txt_senha_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_8.addWidget(self.txt_senha_2)

        self.btn_senha_2 = QPushButton(self.pg_cadastro)
        self.btn_senha_2.setObjectName(u"btn_senha_2")
        self.btn_senha_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(170, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_senha_2)

        self.n_senha_2 = QPushButton(self.pg_cadastro)
        self.n_senha_2.setObjectName(u"n_senha_2")
        self.n_senha_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(170, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_8.addWidget(self.n_senha_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_perfil.sizePolicy().hasHeightForWidth())
        self.cb_perfil.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.cb_perfil.setFont(font3)
        self.cb_perfil.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.cb_perfil)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 35))
        self.btn_cadastrar.setMaximumSize(QSize(200, 16777215))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 10);\n"
"	border-radius: 5px;\n"
"	font-size: 16px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	color: black;\n"
"	background-color: rgb(165, 255, 210);\n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.label_13)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.stackedWidget.addWidget(self.pg_cadastro)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1136, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"TABLES", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">ESTOQUE</span></p></body></html>", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(12, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Especie", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Cod Item", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Municipio", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Serie", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">SA\u00cdDA</span></p></body></html>", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"USU\u00c1RIO", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"DATA IMPORTA\u00c7\u00c3O", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"SERIE", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar Sa\u00edda", None))
        self.btn_estornar.setText(QCoreApplication.translate("MainWindow", u"Estorno", None))
        self.btn_importar.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"Base", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">ESTOQUE</span></p></body></html>", None))
        self.btn_grafico.setText(QCoreApplication.translate("MainWindow", u"Gerar Gr\u00e1fico", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Exel", None))
        self.txt_filtro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Contato</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Desenvolvedor: </span><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Erik Proen\u00e7a</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">(11) 9 8616-5932</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">erik@erikproenca.me</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Sobre</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Este sistema faz a importa\u00e7\u00e3o de arquivos XML e faz</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">o controle do estoque de acordo com a entrada de</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">notas e sa\u00eddas apontadas pelo usu\u00e1rio.</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#064d00;\">STOCK CONTROL</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Created by </span><span style=\" font-size:24pt; color:#6f0000;\">Erik Proen\u00e7a</span></p></body></html>", None))
        self.btn_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">IMPORTAR XML</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta com arquivos XML ---->", None))
        self.btn_open_2.setText(QCoreApplication.translate("MainWindow", u"ABRIR", None))
        self.label_5.setText("")
        self.btn_import_xml.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.label_9.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Tela de Cadastro", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"\"/></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Cadastrar Usu\u00e1rio</span></p></body></html>", None))
        self.nome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Nome</span></p></body></html>", None))
        self.usuario.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Usu\u00e1rio</span></p></body></html>", None))
        self.senha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Senha</span></p></body></html>", None))
        self.btn_senha.setText(QCoreApplication.translate("MainWindow", u"ver", None))
        self.n_senha.setText(QCoreApplication.translate("MainWindow", u"\u00f1 ver", None))
        self.senha_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Senha</span></p></body></html>", None))
        self.btn_senha_2.setText(QCoreApplication.translate("MainWindow", u"ver", None))
        self.n_senha_2.setText(QCoreApplication.translate("MainWindow", u"\u00f1 ver", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Perfil</span></p></body></html>", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_12.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_13.setText("")
    # retranslateUi

