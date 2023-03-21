from PySide2.QtWidgets import *
from login import Ui_Login
from stock_control import Ui_MainWindow
import sys


class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Login do Sistema')
        self.btn_login.clicked.connect(self.open_system)
        
    def open_system(self):
        if self.txt_password.text() == '123':
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            print('Senha inválida')


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Controle de Estoque')
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())
    