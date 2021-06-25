
from PyQt5.QtWidgets import QMainWindow, QHeaderView
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
        window.buttonBox.clicked.connect(lambda :self.createFileAll(window))
        window.actionmysql.triggered.connect(lambda: self.saveConnection(window))
        window.action.triggered.connect(lambda: self.showLinkList(window))
        window.comboBox.currentIndexChanged.connect(lambda: self.writtingTable(window.comboBox.currentText(),window))
        window.comboBox_2.currentIndexChanged.connect(lambda: self.writtingTables(window.comboBox.currentText(),window))
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
        pathName=window.lineEdit_3.text()
        savePath=window.lineEdit_4.text()
        frameWork=window.checkBox_3.isChecked() #mybatisplus
        isEnum=window.checkBox_2.isChecked() #枚举
        lombok=window.checkBox.isChecked() #lombok
        isJPA=window.checkBox_4.isChecked()#jpa checkBox_4
        tableName=window.comboBox_2.currentText()
        sqlData=window.comboBox.currentText()
        isCreateFile=window.checkBox_5.isChecked()#只生成文件
        createData=createCodeData(tableName,pathName,savePath,frameWork,isEnum,lombok,isJPA,isCreateFile,sqlData)
        self.createFile = createFile()
        self.createFile.createFileByPath(createData)
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
    def writtingTable(self, tag,mainWind):
        if tag !='请选择数据源':
            save = TinyDB("AllSaveData.json")
            myCreate = save.table("myConnetion")
            Q = Query()
            data=myCreate.search(Q.name == tag)
            get=getMysqlData(data[0].get("ip"),data[0].get("port"),data[0].get("dbbase"),data[0].get("username"),data[0].get("password"))
            get.getDataFromMysql(mainWind)
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





