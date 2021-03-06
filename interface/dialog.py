from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget

import sys


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(600, 800)
        Register.setMinimumSize(QtCore.QSize(600, 800))
        Register.setMaximumSize(QtCore.QSize(600, 800))
        Register.setStyleSheet("background-color: rgb(67, 67, 67);")
        self.label = QtWidgets.QLabel(Register)
        self.label.setGeometry(QtCore.QRect(230, 302, 60, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_eda = QtWidgets.QLabel(Register)
        self.label_eda.setGeometry(QtCore.QRect(210, 90, 181, 100))
        font = QtGui.QFont()
        font.setFamily("SF Collegiate")
        font.setPointSize(47)
        self.label_eda.setFont(font)
        self.label_eda.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_eda.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_eda.setObjectName("label_eda")
        self.label_2 = QtWidgets.QLabel(Register)
        self.label_2.setGeometry(QtCore.QRect(220, 352, 72, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Register)
        self.label_3.setGeometry(QtCore.QRect(70, 402, 221, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Register)
        self.pushButton.setGeometry(QtCore.QRect(200, 580, 200, 61))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(116, 116, 116);")
        self.pushButton.setObjectName("pushButton")
        self.btn_back = QtWidgets.QPushButton(Register)
        self.btn_back.setGeometry(QtCore.QRect(270, 500, 61, 31))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("color: rgb(255, 255, 255); \n"
"background-color: rgb(67, 67, 67);")
        self.btn_back.setObjectName("btn_back")
        self.textEdit = QtWidgets.QLineEdit(Register)
        self.textEdit.setGeometry(QtCore.QRect(300, 300, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QLineEdit(Register)
        self.textEdit_2.setGeometry(QtCore.QRect(300, 350, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QLineEdit(Register)
        self.textEdit_3.setGeometry(QtCore.QRect(300, 400, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_3.setObjectName("textEdit_3")

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "??????????????????????"))
        self.label.setText(_translate("Register", "??????????:"))
        self.label_eda.setText(_translate("Register", "eda-fit"))
        self.label_2.setText(_translate("Register", "????????????:"))
        self.label_3.setText(_translate("Register", "?????????????????? ???????? ????????????:"))
        self.pushButton.setText(_translate("Register", "????????????"))
        self.btn_back.setText(_translate("Register", "??????????"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QDialog()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())
