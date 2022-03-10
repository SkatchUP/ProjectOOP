import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget

import sys
import Main
import dialog


class DialogWindow(QtWidgets.QDialog, dialog.Ui_Register):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.send_registration)

    # def return_main_window(self):
    #     self.close()
    #     self.main = MainWindow()
    #     self.main.show()

    def send_registration(self):
        login = self.textEdit.text()
        password = self.textEdit_2.text()
        return_password = self.textEdit_3.text()
        data = {'login': login, 'password': password, 'return_password': return_password}
        try:
            response = requests.post('http://127.0.0.1:5000/registration', json=data)
        except:
            return
        if response.status_code == 400:
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
        self.btn_register.clicked.connect(self.start_dialog)

    def start_dialog(self):
        self.close()
        self.dialog = DialogWindow()
        self.dialog.show()


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec_()