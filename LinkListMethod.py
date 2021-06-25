from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QMenu, QHeaderView
from PyQt5.uic.Compiler.qtproxies import QtGui
from tinydb import TinyDB, where


class linkListMothod():
    def __init__(self, window, mainWind):
        self.setLinkListData(window,mainWind)

    def setLinkListData(self,window,mainWind):
        self.window=window
        self.mainWind=mainWind
        save = TinyDB("AllSaveData.json")
        myCreate = save.table("myConnetion")
        data = sorted(myCreate.all(), key=lambda k: k['createTime'])
        for var,index in enumerate(data):
            row=self.window.tableWidget.rowCount()+1;
            self.window.tableWidget.setRowCount(row)
            self.window.tableWidget.setItem(var, 0, QTableWidgetItem(str(index.get("name"))))
            self.window.tableWidget.setItem(var, 1, QTableWidgetItem(str(index.get("ip"))))
            self.window.tableWidget.setItem(var, 2, QTableWidgetItem(str(index.get("port"))))
            self.window.tableWidget.setItem(var, 3, QTableWidgetItem(str(index.get("dbbase"))))
            self.window.tableWidget.setItem(var, 4, QTableWidgetItem(str(index.get("username"))))
        self.window.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.window.tableWidget.customContextMenuRequested.connect(self.generateMenus)
    def generateMenus(self, pos):
        row_num = -1
        for i in self.window.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num >= 0:
            menu = QMenu()
            item1 = menu.addAction(u"删除")
            action = menu.exec_(self.window.tableWidget.mapToGlobal(pos))
            if action == item1:
                text = self.window.tableWidget.item(row_num, 0).text()
                save = TinyDB("AllSaveData.json")
                myCreate = save.table("myConnetion")
                myCreate.remove(where('name')==str(text))
                self.window.tableWidget.setRowCount(0)
                self.setLinkListData(self.window,self.mainWind)
                self.mainWind.comboBox.removeItem(row_num+1);
                menu.clear()
                return;
            else:
                menu.clear()
                return;
            menu.clear()

