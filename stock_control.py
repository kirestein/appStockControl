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

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")

        self.horizontalLayout.addWidget(self.btn_contato)

        self.btn_outro = QPushButton(self.frame)
        self.btn_outro.setObjectName(u"btn_outro")

        self.horizontalLayout.addWidget(self.btn_outro)


        self.verticalLayout_2.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.verticalLayout_8 = QVBoxLayout(self.pg_table)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.pg_table)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout_7 = QVBoxLayout(self.tables)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_file = QLineEdit(self.tables)
        self.txt_file.setObjectName(u"txt_file")

        self.horizontalLayout_2.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.tables)
        self.btn_open.setObjectName(u"btn_open")

        self.horizontalLayout_2.addWidget(self.btn_open)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

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
        self.btn_importar = QPushButton(self.frame_2)
        self.btn_importar.setObjectName(u"btn_importar")

        self.verticalLayout_3.addWidget(self.btn_importar)

        self.btn_gerar = QPushButton(self.frame_2)
        self.btn_gerar.setObjectName(u"btn_gerar")

        self.verticalLayout_3.addWidget(self.btn_gerar)

        self.btn_estornar = QPushButton(self.frame_2)
        self.btn_estornar.setObjectName(u"btn_estornar")

        self.verticalLayout_3.addWidget(self.btn_estornar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.pg_table)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout = QVBoxLayout(self.pg_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.label)

        self.stackedWidget.addWidget(self.pg_home)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_9 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_14 = QLabel(self.pg_cadastro)
        self.label_14.setObjectName(u"label_14")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_14)

        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.nome = QLabel(self.pg_cadastro)
        self.nome.setObjectName(u"nome")

        self.horizontalLayout_5.addWidget(self.nome)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")

        self.horizontalLayout_5.addWidget(self.txt_nome)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.usuario = QLabel(self.pg_cadastro)
        self.usuario.setObjectName(u"usuario")

        self.horizontalLayout_6.addWidget(self.usuario)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")

        self.horizontalLayout_6.addWidget(self.txt_usuario)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.senha = QLabel(self.pg_cadastro)
        self.senha.setObjectName(u"senha")

        self.horizontalLayout_7.addWidget(self.senha)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")

        self.horizontalLayout_7.addWidget(self.txt_senha)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.txt_senha_2 = QLabel(self.pg_cadastro)
        self.txt_senha_2.setObjectName(u"txt_senha_2")

        self.horizontalLayout_8.addWidget(self.txt_senha_2)

        self.lineEdit_4 = QLineEdit(self.pg_cadastro)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_8.addWidget(self.lineEdit_4)


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

        self.horizontalLayout_9.addWidget(self.cb_perfil)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")

        self.horizontalLayout_10.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.stackedWidget.addWidget(self.pg_cadastro)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.btn_cadastro = QPushButton(self.centralwidget)
        self.btn_cadastro.setObjectName(u"btn_cadastro")

        self.horizontalLayout_4.addWidget(self.btn_cadastro)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)


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

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"TABLES", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.btn_outro.setText(QCoreApplication.translate("MainWindow", u"OUTRO", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SA\u00cdDA", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"USU\u00c1RIO", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"DATA IMPORTA\u00c7\u00c3O", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"SERIE", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.btn_importar.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar Sa\u00edda", None))
        self.btn_estornar.setText(QCoreApplication.translate("MainWindow", u"Estorno", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"TreeWidget", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#064d00;\">STOCK CONTROL</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Created by </span><span style=\" font-size:24pt; color:#6f0000;\">Erik Proen\u00e7a</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Tela de Cadastro", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.nome.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.usuario.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.senha.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.txt_senha_2.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Perfil", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_12.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_13.setText("")
        self.label_4.setText("")
        self.btn_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_5.setText("")
    # retranslateUi

