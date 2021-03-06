import os
import re
from  CreateFileContent import createFileDataContent


class createFile():
    def createFileByPath(self,createCodeData):
        FileContent = createFileDataContent()
        isCreateFile = createCodeData.isCreateFile
        createTableName=self.dealTableName(createCodeData.tableName)
        if createCodeData is None:
            return

        pageName="main\\java\\"+createCodeData.pathName
        pageName=pageName.replace(".","\\")
        #生成总目录
        path=createCodeData.savePath+"\\代码生成目录"
        folder = os.path.exists(path)
        if not folder :
            os.mkdir(path)

        path=createCodeData.savePath+"\\代码生成目录\\"+pageName
        split = path.split("\\", -1)
        allPath=""
        for paths in split:
            if allPath !="":
                allPath=allPath+"//"+paths
            else:
                allPath=paths
            folder = os.path.exists(allPath)
            if not folder :
                os.mkdir(allPath)
        path = createCodeData.savePath + "\\代码生成目录\\"+pageName+"\\entity"
        folder = os.path.exists(path)
        if not folder:
            os.mkdir(path)
            file = open(createCodeData.savePath + "\\代码生成目录\\"+pageName+"\\entity\\"+createTableName+"Vo.java", 'w',encoding='utf-8')
            if isCreateFile !=True:
                controllers = FileContent.createEntity(createCodeData, createTableName)
                file.write(controllers)
            file.close()
        #生成controller
        path = createCodeData.savePath + "\\代码生成目录\\"+pageName+"\\controller"
        folder = os.path.exists(path)
        if not folder:
            os.mkdir(path)
            file = open(createCodeData.savePath + "\\代码生成目录\\"+pageName+"\\controller\\"+createTableName+"Controller.java", 'w',encoding='utf-8')
            controllers = FileContent.createController(createCodeData, createTableName)
            file.write(controllers)
            file.close()
        #生成service
        path = createCodeData.savePath + "\\代码生成目录\\"+pageName+"\\service"
        folder = os.path.exists(path)
        if not folder:
            os.mkdir(path)
            file = open(
                createCodeData.savePath + "\\代码生成目录\\"+pageName+"\\service\\" + createTableName + "Service.java",
                'w',encoding='utf-8')
            if isCreateFile !=True:
                controllers = FileContent.createService(createCodeData, createTableName)
                file.write(controllers)
            file.close()
        #生成impl
        path = createCodeData.savePath + "\\代码生成目录\\"+pageName+"\\service\\impl"
        folder = os.path.exists(path)
        if not folder:
            os.mkdir(path)
            file = open(
                createCodeData.savePath + "\\代码生成目录\\"+pageName+"\\service\\impl\\" +createTableName + "ServiceImpl.java",
                'w',encoding='utf-8')
            if isCreateFile !=True:
                controllers = FileContent.createServiceImpl(createCodeData, createTableName)
                file.write(controllers)
            file.close()
        #生成Mapper
        path = createCodeData.savePath + "\\代码生成目录\\"+pageName+"\\mapper"
        folder = os.path.exists(path)
        if not folder:
            os.mkdir(path)
            file = open(
                createCodeData.savePath + "\\代码生成目录\\"+pageName+"\\mapper\\" +createTableName+ "Mapper.java",
                'w',encoding='utf-8')
            if isCreateFile !=True:
                controllers = FileContent.createDaoMapper(createCodeData, createTableName)
                file.write(controllers)
            file.close()

        path = createCodeData.savePath + "\\代码生成目录\\resources"
        folder = os.path.exists(path)
        if not folder:
            os.mkdir(path)
        path = createCodeData.savePath + "\\代码生成目录\\resources\\mybatis"
        folder = os.path.exists(path)
        if not folder:
            os.mkdir(path)
            file = open(
                createCodeData.savePath + "\\代码生成目录\\resources\\mybatis\\" +createTableName + "Mapper.xml",
                'w',encoding='utf-8')
            if isCreateFile !=True:
                controllers = FileContent.createDaoMapperXml(createCodeData, createTableName)
                file.write(controllers)
            file.close()
    def dealTableName(self,tableName):
        tableName=tableName.strip()
        split = tableName.split("_",-1)
        tableName=""
        for ind in split:
            tableName=tableName+ind.capitalize()
        tableName = re.sub('\W+', '', tableName).replace("_", '')
        pattern = re.compile(r'[\u4e00-\u9fa5]')
        tableName = re.sub(pattern,"",tableName)
        return tableName











