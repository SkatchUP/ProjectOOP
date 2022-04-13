import interface.Start_window
from PyQt5 import QtWidgets


class StartWindow(QtWidgets.QMainWindow, interface.Start_window.Ui_StartWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
