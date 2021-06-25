import time

from PyQt5.QtWidgets import QMessageBox, QWidget
from tinydb import TinyDB, Query

from GetDirFilePath import getDirFilePath


class saveConnectionMethod():
    def __init__(self, window, mainWind):
        self.getDirPath = getDirFilePath(None)
        window.buttonBox.clicked.connect(lambda: self.saveConnection(window, mainWind))
    def saveConnection(self, window, mainWind):
        self.ip = window.lineEdit.text()  # ip
        self.port = window.lineEdit_2.text()  # 端口号
        self.userName = window.lineEdit_3.text()  # 用户名
        self.password = window.lineEdit_4.text()  # 密码
        self.dbBase = window.lineEdit_6.text()  # 库名
        self.name = window.lineEdit_7.text()  # 库名
        save = TinyDB("AllSaveData.json")
        myCreate = save.table("myConnetion")
        Q = Query()
        search = myCreate.search((Q.name == self.name))
        if len(search)>0:
            button = QMessageBox.Close
            q_widget = QWidget()
            QMessageBox.critical(q_widget,"保存出错","已经定义了改名字的数据库连接！",button)
            return
        myCreate.insert({'ip': self.ip,
                         'port': self.port,
                         'username': self.userName,
                         'password': self.password,
                         'dbbase': self.dbBase,
                         'name': self.name,
                         'createTime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                         })
        mainWind.comboBox.addItem(self.name)
