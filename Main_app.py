from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_app(object):
    def setupUi(self, Main_app):
        Main_app.setObjectName("Main_app")
        Main_app.resize(600, 800)
        Main_app.setMinimumSize(QtCore.QSize(600, 800))
        Main_app.setMaximumSize(QtCore.QSize(600, 800))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        Main_app.setFont(font)
        Main_app.setStyleSheet("background-color: rgb(67, 67, 67);")
        self.centralwidget = QtWidgets.QWidget(Main_app)
        self.centralwidget.setObjectName("centralwidget")
        self.text_eat_month = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_eat_month.setGeometry(QtCore.QRect(300, 60, 281, 671))
        self.text_eat_month.setStyleSheet("background-color: rgb(190, 190, 190);\n"
"border-color: rgb(255, 255, 255);")
        self.text_eat_month.setObjectName("text_eat_month")
        self.label_eat_month = QtWidgets.QLabel(self.centralwidget)
        self.label_eat_month.setGeometry(QtCore.QRect(380, 20, 117, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_eat_month.setFont(font)
        self.label_eat_month.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_eat_month.setObjectName("label_eat_month")
        self.text_eat_today = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_eat_today.setGeometry(QtCore.QRect(20, 60, 256, 131))
        self.text_eat_today.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.text_eat_today.setObjectName("text_eat_today")
        self.label_eat_today = QtWidgets.QLabel(self.centralwidget)
        self.label_eat_today.setGeometry(QtCore.QRect(80, 20, 134, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_eat_today.setFont(font)
        self.label_eat_today.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_eat_today.setObjectName("label_eat_today")
        self.btn_add_eat = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_eat.setGeometry(QtCore.QRect(90, 450, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_add_eat.setFont(font)
        self.btn_add_eat.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(116, 116, 116);")
        self.btn_add_eat.setObjectName("btn_add_eat")
        self.label_add_food = QtWidgets.QLabel(self.centralwidget)
        self.label_add_food.setGeometry(QtCore.QRect(70, 225, 146, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_add_food.setFont(font)
        self.label_add_food.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_add_food.setObjectName("label_add_food")
        self.label_name_add = QtWidgets.QLabel(self.centralwidget)
        self.label_name_add.setGeometry(QtCore.QRect(110, 275, 68, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name_add.setFont(font)
        self.label_name_add.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_name_add.setObjectName("label_name_add")
        self.label_calories = QtWidgets.QLabel(self.centralwidget)
        self.label_calories.setGeometry(QtCore.QRect(90, 355, 113, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_calories.setFont(font)
        self.label_calories.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_calories.setObjectName("label_calories")
        self.text_name = QtWidgets.QLineEdit(self.centralwidget)
        self.text_name.setGeometry(QtCore.QRect(60, 310, 167, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_name.setFont(font)
        self.text_name.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.text_name.setObjectName("text_name")
        self.text_calories = QtWidgets.QLineEdit(self.centralwidget)
        self.text_calories.setGeometry(QtCore.QRect(60, 390, 167, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_calories.setFont(font)
        self.text_calories.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.text_calories.setObjectName("text_calories")
        self.label_del_food = QtWidgets.QLabel(self.centralwidget)
        self.label_del_food.setGeometry(QtCore.QRect(80, 520, 125, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_del_food.setFont(font)
        self.label_del_food.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_del_food.setObjectName("label_del_food")
        self.text_delete = QtWidgets.QLineEdit(self.centralwidget)
        self.text_delete.setGeometry(QtCore.QRect(60, 595, 167, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_delete.setFont(font)
        self.text_delete.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.text_delete.setObjectName("text_delete")
        self.btn_delete_eat = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete_eat.setGeometry(QtCore.QRect(90, 655, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_delete_eat.setFont(font)
        self.btn_delete_eat.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(116, 116, 116);")
        self.btn_delete_eat.setObjectName("btn_delete_eat")
        self.vegit = QtWidgets.QCheckBox(self.centralwidget)
        self.vegit.setGeometry(QtCore.QRect(380, 740, 147, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vegit.setFont(font)
        self.vegit.setStyleSheet("color: rgb(255, 255, 255);")
        self.vegit.setObjectName("vegit")
        self.label_name_add_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_name_add_2.setGeometry(QtCore.QRect(110, 560, 68, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name_add_2.setFont(font)
        self.label_name_add_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_name_add_2.setObjectName("label_name_add_2")
        Main_app.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(Main_app)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.menuBar.setFont(font)
        self.menuBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuBar.setAutoFillBackground(False)
        self.menuBar.setStyleSheet("QMenuBar::item {\n"
"    background-color: rgb(67, 67, 67);\n"
"    color: rgb(255,255,255);  \n"
"}\n"
"QMenuBar::item:selected {    \n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"QMenuBar::item:pressed {\n"
"    background: rgb(150, 150, 150);\n"
"}")
        self.menuBar.setObjectName("menuBar")
        self.settings = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.settings.setFont(font)
        self.settings.setStyleSheet("QMenu {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(120, 120, 120);\n"
"}\n"
"QMenu::item {\n"
"    background-color: transparent;\n"
"}\n"
"QMenu::item:selected { \n"
"    background-color: rgb(150, 150, 150);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.settings.setObjectName("settings")
        Main_app.setMenuBar(self.menuBar)
        self.action_IMT = QtWidgets.QAction(Main_app)
        self.action_IMT.setObjectName("action_IMT")
        self.action_leave = QtWidgets.QAction(Main_app)
        self.action_leave.setObjectName("action_leave")
        self.settings.addAction(self.action_IMT)
        self.settings.addSeparator()
        self.settings.addAction(self.action_leave)
        self.menuBar.addAction(self.settings.menuAction())

        self.retranslateUi(Main_app)
        QtCore.QMetaObject.connectSlotsByName(Main_app)

    def retranslateUi(self, Main_app):
        _translate = QtCore.QCoreApplication.translate
        Main_app.setWindowTitle(_translate("Main_app", "Еда-Фит"))
        self.text_eat_month.setHtml(_translate("Main_app", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_eat_month.setText(_translate("Main_app", "Еда на месяц"))
        self.label_eat_today.setText(_translate("Main_app", "Еда на сегодня"))
        self.btn_add_eat.setText(_translate("Main_app", "Добавить еду"))
        self.label_add_food.setText(_translate("Main_app", "Добавление еды"))
        self.label_name_add.setText(_translate("Main_app", "Название"))
        self.label_calories.setText(_translate("Main_app", "Каллорийность"))
        self.label_del_food.setText(_translate("Main_app", "Удаление еды"))
        self.btn_delete_eat.setText(_translate("Main_app", "Удалить еду"))
        self.vegit.setText(_translate("Main_app", "Режим вегитарианца"))
        self.label_name_add_2.setText(_translate("Main_app", "Название"))
        self.settings.setTitle(_translate("Main_app", "Настройки"))
        self.action_IMT.setText(_translate("Main_app", "Изменить ИМТ"))
        self.action_leave.setText(_translate("Main_app", "Выйти из профиля"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_app = QtWidgets.QMainWindow()
    ui = Ui_Main_app()
    ui.setupUi(Main_app)
    Main_app.show()
    sys.exit(app.exec_())
