import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication, QDialog

import sys
import Main
import dialog

class Errors(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()

    def error_registration(self):
        error_reg = QMessageBox()
        error_reg.setWindowTitle('Error')
        error_reg.setIcon(QMessageBox.Critical)
        error_reg.setText('Ошибка при регистрации')
        error_reg.setInformativeText('Пароли не совпадают')
        error_reg.setStandardButtons(QMessageBox.Ok)
        error_reg.show()
        error_reg.exec_()


class DialogWindow(dialog.Ui_Register, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.send_registration)

    def send_registration(self):
        login = self.textEdit.text()
        password = self.textEdit_2.text()
        return_password = self.textEdit_3.text()
        data = {'login': login, 'password': password, 'return_password': return_password}
        try:
            response = requests.post('http://127.0.0.1:5000/registration', json=data)
        except:
            return
        if response.status_code == 401:
            error = Errors()
            error.error_registration()
        elif response.status_code == 400:
            self.textEdit.setText('Error')
            self.textEdit_2.setText('Error')
            self.textEdit_3.setText('Error')
        else:
            self.close()
            self.main = MainWindow()
            self.main.show()


class MainWindow(QtWidgets.QMainWindow, Main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_register.clicked.connect(self.open_reg)

    def open_reg(self):
        self.close()
        self.start = DialogWindow()
        self.start.show()


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec_()
