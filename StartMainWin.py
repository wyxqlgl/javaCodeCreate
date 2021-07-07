from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QAbstractItemView
import sys
from Method import method
from SaveConnection import SqlMain
from Window import Ui_MainWindow #主页面


class startMainWin():
    def __init__(self):
        self.app=QApplication(sys.argv)
        self.mainWind=QMainWindow()
        self.windows=Ui_MainWindow()
        self.windows.setupUi(self.mainWind)
        self.method = method(self.windows, self.mainWind)
        self.mainWind.show()

        self.app.exit(self.app.exec_())


