from PySide2.QtWidgets import *
from login import Ui_Login
from stock_control import Ui_MainWindow
import sys
from database import DataBase


class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tried = 0
        self.setupUi(self)
        self.setWindowTitle('Login do Sistema')
        self.btn_login.clicked.connect(self.check_login)
        
    
            
    def check_login(self):
        self.users = DataBase()
        self.users.conecta()
        authenticator = self.users.check_user(self.txt_user.text().upper(), self.txt_password.text())
        
        if authenticator.lower() == 'admin' or authenticator.lower() == 'user':
            self.w = MainWindow(authenticator.lower())
            self.w.show()
            self.close()
        else:
            if self.tried < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle('Acesso negado')
                msg.setText(f'Usuário ou senha incorreto! \n \n Tentativa: {self.tried + 1} de 3')
                msg.exec_()
                self.tried += 1
                
            if self.tried == 3:
                #fazer o codigo para bloquear o usuário
                self.users.close_connection()
                sys.exit(0)


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, user) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Controle de Estoque')
        
        if user.lower() == 'user':
            self.btn_cadastro.setVisible(False)
        #****************** SYSTEM PAGES ******************#
        self.btn_home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_home))
        self.btn_tables.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_tables))
        self.btn_contato.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_contato))
        self.btn_sobre.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_sobre))
        self.btn_cadastro.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_cadastro))
        # self.btn_senha.clicked.connect(lambda: self.txt_senha.setEchoMode(QLineEdit.Normal))
        # self.n_senha.clicked.connect(lambda: self.txt_senha.setEchoMode(QLineEdit.Password))
        # self.btn_senha_2.clicked.connect(lambda: self.txt_senha_2.setEchoMode(QLineEdit.Normal))
        # self.n_senha_2.clicked.connect(lambda: self.txt_senha_2.setEchoMode(QLineEdit.Password))
        
        self.btn_cadastrar.clicked.connect(self.subscribe_user)
        
        
    def subscribe_user(self):
        senha1 = self.txt_senha.text()
        senha2 = self.txt_senha_2.text()
        
        if senha1 != senha2:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Senhas divergentes')
            msg.setText(f'As senhas estão diferentes!! Senha 1 = {senha1}, senha 2 = {senha2}')
            msg.exec_()
            
            return None
        
            
        nome = self.txt_nome.text()
        user = self.txt_usuario.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()
        
        db = DataBase()
        db.conecta()
        db.insert_user(nome, user, password, access)
        db.close_connection()
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Cadastro realizado')
        msg.setText('Usuário cadastrado com sucesso!!')
        msg.exec_()
        
        self.txt_nome.setText('')
        self.txt_usuario.setText('')
        self.txt_senha.setText('')
        self.txt_senha_2.setText('')
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())
    