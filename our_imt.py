from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import math_func


class Ui_IMT(object):
    def setupUi(self, IMT):
        IMT.setObjectName("IMT")
        IMT.resize(600, 800)
        IMT.setMinimumSize(QtCore.QSize(600, 800))
        IMT.setMaximumSize(QtCore.QSize(600, 800))
        IMT.setStyleSheet("background-color: rgb(67, 67, 67);")
        self.centralwidget = QtWidgets.QWidget(IMT)
        self.centralwidget.setObjectName("centralwidget")
        self.label_eda = QtWidgets.QLabel(self.centralwidget)
        self.label_eda.setGeometry(QtCore.QRect(210, 90, 181, 100))
        font = QtGui.QFont()
        font.setFamily("SF Collegiate")
        font.setPointSize(47)
        self.label_eda.setFont(font)
        self.label_eda.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_eda.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_eda.setObjectName("label_eda")
        self.textEdit_weight = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_weight.setGeometry(QtCore.QRect(345, 315, 41, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_weight.setFont(font)
        self.textEdit_weight.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_weight.setObjectName("textEdit_weight")
        self.label_weight = QtWidgets.QLabel(self.centralwidget)
        self.label_weight.setGeometry(QtCore.QRect(180, 317, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_weight.setFont(font)
        self.label_weight.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_weight.setObjectName("label_weight")
        self.label_height = QtWidgets.QLabel(self.centralwidget)
        self.label_height.setGeometry(QtCore.QRect(170, 393, 171, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_height.setFont(font)
        self.label_height.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_height.setObjectName("label_height")
        self.label_sm = QtWidgets.QLabel(self.centralwidget)
        self.label_sm.setGeometry(QtCore.QRect(390, 393, 27, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_sm.setFont(font)
        self.label_sm.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_sm.setObjectName("label_sm")
        self.textEdit_height = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_height.setGeometry(QtCore.QRect(345, 390, 41, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_height.setFont(font)
        self.textEdit_height.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_height.setObjectName("textEdit_height")
        self.label_kg = QtWidgets.QLabel(self.centralwidget)
        self.label_kg.setGeometry(QtCore.QRect(390, 317, 23, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_kg.setFont(font)
        self.label_kg.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_kg.setObjectName("label_kg")
        self.btn_ready = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ready.setGeometry(QtCore.QRect(200, 550, 200, 61))
        self.btn_ready.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(116, 116, 116);")
        self.btn_ready.setObjectName("btn_ready")
        self.label_IMT = QtWidgets.QLabel(self.centralwidget)
        self.label_IMT.setGeometry(QtCore.QRect(172, 220, 256, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_IMT.setFont(font)
        self.label_IMT.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_IMT.setObjectName("label_IMT")
        IMT.setCentralWidget(self.centralwidget)

        self.retranslateUi(IMT)
        QtCore.QMetaObject.connectSlotsByName(IMT)

    def retranslateUi(self, IMT):
        _translate = QtCore.QCoreApplication.translate
        IMT.setWindowTitle(_translate("IMT", "ИМТ"))
        self.label_eda.setText(_translate("IMT", "eda-fit"))
        self.label_weight.setText(_translate("IMT", "Введите свой вес:"))
        self.label_height.setText(_translate("IMT", "Введите свой рост:"))
        self.label_sm.setText(_translate("IMT", "см."))
        self.label_kg.setText(_translate("IMT", "кг."))
        self.btn_ready.setText(_translate("IMT", "Готово"))
        self.label_IMT.setText(_translate("IMT", "Высчитаем ваш ИМТ"))
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IMT = QtWidgets.QMainWindow()
    ui = Ui_IMT()
    ui.setupUi(IMT)
    IMT.show()
    sys.exit(app.exec_())
