import os,shutil
import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget, QMainWindow, QHeaderView
from tinydb import TinyDB, Query

from CreateCodeData import createCodeData
from CreateFile import createFile
from GetDirFilePath import getDirFilePath
from LinkList import linkList
from GetMysqlData import getMysqlData
from LinkListMethod import linkListMothod
from SaveConnection import SqlMain
from SaveConnectionMethod import saveConnectionMethod
class method():
    def __init__(self,window,mainWind):
        self.getDirPath= getDirFilePath(None)
        window.toolButton_3.clicked.connect(lambda :self.chooseDir(window,mainWind))
        window.toolButton.clicked.connect(lambda :self.createFileAll(window))
        window.actionmysql.triggered.connect(lambda: self.saveConnection(window))
        window.action.triggered.connect(lambda: self.showLinkList(window))
        window.comboBox.currentIndexChanged.connect(lambda: self.writtingTable(window.comboBox.currentText(),window,mainWind))
        window.comboBox_2.currentIndexChanged.connect(lambda: self.writtingTables(window.comboBox.currentText(),window))
        window.toolButton_4.clicked.connect(lambda :self.delPath(window))
        self.getData(window)
    def saveConnection(self,mainWind):

        self.mainWindSql = QMainWindow()
        self.windowsSql = SqlMain()
        self.windowsSql.setupUi(self.mainWindSql)
        self.saveConnectionMethod= saveConnectionMethod(self.windowsSql, mainWind)
        self.mainWindSql.show()
    def showLinkList(self,mainwind):
        self.linkLists = QMainWindow()
        self.windowslinkList = linkList()
        self.windowslinkList.setupUi(self.linkLists)
        self.linklistmethod=linkListMothod(self.windowslinkList,mainwind)
        self.windowslinkList.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.windowslinkList.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.linkLists.show()
    def createFileAll(self,window):
       try:
           pathName=window.lineEdit_3.text()
           savePath=window.lineEdit_4.text()
           oauther=window.lineEdit.text()
           frameWork=window.checkBox_3.isChecked() #mybatisplus
           lombok=window.checkBox.isChecked() #lombok
           isJPA=window.checkBox_4.isChecked()#jpa checkBox_4
           tableName=window.comboBox_2.currentText()
           sqlData=window.comboBox.currentText()
           isCreateFile=window.checkBox_5.isChecked()#只生成文件
           createData=createCodeData(tableName,pathName,savePath,frameWork,lombok,isJPA,isCreateFile,sqlData,oauther)
           self.createFile = createFile()
           self.createFile.createFileByPath(createData)
           QMessageBox.about(None, "提示！！", "生成文件成功！")
       except Exception:
           QMessageBox.critical(None, "提示！！", "生成文件失败！")
    def chooseDir(self,window,mainWind):
        mainWind.hide()
        dirPath=self.getDirPath.chooseDir()
        mainWind.show()
        window.lineEdit_4.setText(dirPath)
    def getData(self,mainWind):
        save = TinyDB("AllSaveData.json")
        myCreate = save.table("myConnetion")
        data=myCreate.all()
        for var in data:
            mainWind.comboBox.addItem(var.get("name"))
    def writtingTable(self, tag,window,mainWind):
        if tag !='请选择数据源':
            save = TinyDB("AllSaveData.json")
            myCreate = save.table("myConnetion")
            Q = Query()
            data=myCreate.search(Q.name == tag)
            get=getMysqlData(data[0].get("ip"),data[0].get("port"),data[0].get("dbbase"),data[0].get("username"),data[0].get("password"))
            try:
                get.getDataFromMysql(window)
            except  Exception:
                QMessageBox.critical(None, "错误", "链接数据库错误,请检查链接！！")

        else:
            mainWind.comboBox_2.clear()
            mainWind.comboBox_2.addItem("选择表")
    def writtingTables(self, tag,mainWind):
        if tag !='请选择数据源':
            save = TinyDB("AllSaveData.json")
            myCreate = save.table("myConnetion")
            Q = Query()
            data=myCreate.search(Q.name == tag)
            get=getMysqlData(data[0].get("ip"),data[0].get("port"),data[0].get("dbbase"),data[0].get("username"),data[0].get("password"))
            get.getTableFiled(mainWind)
        else:
            mainWind.comboBox_2.clear()
            mainWind.comboBox_2.addItem("选择表")
    def delPath(self,window,ismassage=None):
        if  window.lineEdit_4.text()=='' or window.lineEdit_4.text() is None:
            QMessageBox.about(None, "提示！！", "先选择生成路径！")
            return
        path = window.lineEdit_4.text()+"\\代码生成目录"
        folder = os.path.exists(path)
        if  folder :
            del_list = os.listdir(path)
            for f in del_list:
                file_path = os.path.join(path, f)
                if os.path.isfile(file_path):
                    try:
                        os.remove(file_path)
                    except Exception:
                        continue
                elif os.path.isdir(file_path):
                    try:
                        shutil.rmtree(file_path)
                    except Exception:
                       continue
            try:
                time.sleep(1) # 休眠1秒
                shutil.rmtree(path)
            except Exception:
                time.sleep(1) # 休眠1秒
                self.delPath(window,1)
            if ismassage is  None:
                QMessageBox.about(None, "提示！！", "删除文件成功！")
        else:
            QMessageBox.about(None, "提示！！", "没有这个文件！")






