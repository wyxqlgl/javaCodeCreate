import os
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QFileDialog

class getDirFilePath(QWidget):
    def __init__(self, parent=None, name = 'MainForm'):
        super(getDirFilePath,self).__init__(parent)
        self.setWindowTitle(name)
        self.cwd = os.getcwd() # 获取当前程序文件位置
        self.resize(300,200)   # 设置窗体大小
        # btn 1
        self.btn_chooseDir = QPushButton(self)
        self.btn_chooseDir.setObjectName("btn_chooseDir")
        self.btn_chooseDir.setText("选择文件夹")

    def chooseDir(self):
        dir_choose = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      self.cwd)  # 起始路径
        if dir_choose == "":
            print("\n取消选择")
            return
        return dir_choose
    def chooseSqlFile(self):
        file_choose,filt=QFileDialog.getOpenFileName(self,"打开文件",self.cwd,"sql文件(*.sql)")
        return file_choose


