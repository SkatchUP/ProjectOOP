import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication, QDialog

import sys
import math_func
import Main_app
import interface.Start_window
import interface.dialog
import interface.our_imt

# основное окно
class MainAPP(QtWidgets.QMainWindow, Main_app.Ui_Main_app):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.id_user = id[5:]
        self.label_eat_month.setObjectName(f'user_{self.id_user}')
        self.action_IMT.triggered.connect(self.new_imt)
    
    def new_imt(self):
        self.close()
        self.change_imt = IMT_window()
        self.change_imt.show()

# класс со всеми вылезающими ошибками
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

    def error_imt_compute(self):
        error_imt = QMessageBox()
        error_imt.setWindowTitle('Error')
        error_imt.setIcon(QMessageBox.Critical)
        error_imt.setText('Ошибка расчета ИМТ')
        error_imt.setInformativeText('Вы не ввели данные')
        error_imt.setStandardButtons(QMessageBox.Ok)
        error_imt.show()
        error_imt.exec_()
    
    def error_sign_in(self):
        error_reg = QMessageBox()
        error_reg.setWindowTitle('Error')
        error_reg.setIcon(QMessageBox.Critical)
        error_reg.setText('Ошибка при входе в акканут')
        error_reg.setInformativeText('Логин и пароль не совпадают')
        error_reg.setStandardButtons(QMessageBox.Ok)
        error_reg.show()
        error_reg.exec_()

# окно рачета ИМТ
class IMT_window(QtWidgets.QMainWindow, interface.our_imt.Ui_IMT):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_ready.clicked.connect(self.math)
        try:
            get_response = requests.get('http://127.0.0.1:5000/sign_in').json()
        except:
            return
        self.label_eda.setObjectName(f"user_{get_response['id_login'][0]}")
        self.chek = f"user_{get_response['id_login'][0]}"

    def math(self):
        if self.textEdit_height.text() == '' or self.textEdit_weight.text() == '':
            error = Errors()
            error.error_imt_compute()
        else:
            try: 
                response = requests.post('http://127.0.0.1:5000/chek', json=self.chek)
            except:
                return
            num_imt = math_func.imt(self)
            if response.status_code == 200:
                data = {'id_imt': self.label_eda.objectName(), 'imt': num_imt}
                try:
                    requests.post('http://127.0.0.1:5000/imt', json=data)
                except:
                    return
                self.close()
                self.app = MainAPP(self.label_eda.objectName())
                self.app.show()
            elif response.status_code == 300:
                data = {'id_imt': self.label_eda.objectName(), 'changed_imt': num_imt}
                try:
                    requests.post('http://127.0.0.1:5000/change_imt', json=data)
                except:
                    return
                self.close()
                self.app = MainAPP(self.label_eda.objectName())
                self.app.show()

# окно регистрации
class DialogWindow(interface.dialog.Ui_Register, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.send_registration)
        self.btn_back.clicked.connect(self.returnback)

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
            self.main = StartWindow()
            self.main.show()

    def returnback(self):
        self.close()
        self.main = StartWindow()
        self.main.show()

# стартовое окно
class StartWindow(QtWidgets.QMainWindow, interface.Start_window.Ui_StartWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_register.clicked.connect(self.open_reg)
        self.btn_next1.clicked.connect(self.next_step)

    def open_reg(self):
        self.close()
        self.start = DialogWindow()
        self.start.show()

    def next_step(self):
        login = self.login.text()
        password = self.password.text()
        data = {'login': login, 'password': password}
        try: 
            response = requests.post('http://127.0.0.1:5000/sign_in', json=data)
        except:
            return

        if response.status_code == 200:
            self.close()
            self.open = IMT_window()
            self.open.show()
        elif response.status_code == 300:
            try:
                get_response = requests.get('http://127.0.0.1:5000/sign_in').json()
            except:
                return
            id_user = f"user_{get_response['id_login'][0]}"
            self.close()
            self.open = MainAPP(id_user)
            self.open.show()


app = QtWidgets.QApplication([])
window = StartWindow()
window.show()
app.exec_()
