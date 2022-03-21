import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication

import sys
import Main
import dialog


class MainWindow(Main.Ui_MainWindow, dialog.Ui_Register):
    def __init__(self):
        super().setupUi(self)
        self.btn_register.clicked.connect(self.open_reg)

    def open_reg(self):
        self.close()
        self.start = dialog.Ui_Register()
        self.start.show()


class Register(dialog.Ui_Register):
    def __init__(self):
        super().setupUi_reg()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# app = MainWindow()
# app.show()
# app = QtWidgets.QApplication([])
# window = MainWindow()
# window.show()
# app.exec_()
