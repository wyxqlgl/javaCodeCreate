import os
import re
from  CreateFileContent import createFileDataContent


class createFile():
    def createFileByPath(self,createCodeData):
        FileContent = createFileDataContent()
        createTableName=self.dealTableName(createCodeData.tableName)
        if createCodeData is None:
            return

        pageName="main\\java\\"+createCodeData.pathName
        pageName=pageName.replace(".","\\")
        #生成总目录
        path=createCodeData.savePath+"\\CreateAllFileInThePath"
        folder = os.path.exists(path)
        if not folder :
            os.mkdir(path)

        path=createCodeData.savePath+"\\CreateAllFileInThePath\\"+pageName
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
        path = createCodeData.savePath + "\\CreateAllFileInThePath\\"+pageName+"\\entity"
        folder = os.path.exists(path)
        if not folder:
            os.mkdir(path)
            file = open(createCodeData.savePath + "\\CreateAllFileInThePath\\"+pageName+"\\entity\\"+createTableName+"Vo.java", 'w')
            controllers = FileContent.createEntity(createCodeData, createTableName)
            file.write(controllers)
            file.close()
        #生成controller
        path = createCodeData.savePath + "\\CreateAllFileInThePath\\"+pageName+"\\controller"
        folder = os.path.exists(path)
        if not folder:
            os.mkdir(path)
            file = open(createCodeData.savePath + "\\CreateAllFileInThePath\\"+pageName+"\\controller\\"+createTableName+"Controller.java", 'w')
            controllers = FileContent.createController(createCodeData, createTableName)
            file.write(controllers)
            file.close()
        #生成service
        path = createCodeData.savePath + "\\CreateAllFileInThePath\\"+pageName+"\\service"
        folder = os.path.exists(path)
        if not folder:
            os.mkdir(path)
            file = open(
                createCodeData.savePath + "\\CreateAllFileInThePath\\"+pageName+"\\service\\" + createTableName + "Service.java",
                'w')
            controllers = FileContent.createService(createCodeData, createTableName)
            file.write(controllers)
            file.close()
        #生成impl
        path = createCodeData.savePath + "\\CreateAllFileInThePath\\"+pageName+"\\service\\impl"
        folder = os.path.exists(path)
        if not folder:
            os.mkdir(path)
            file = open(
                createCodeData.savePath + "\\CreateAllFileInThePath\\"+pageName+"\\service\\impl\\" +createTableName + "ServiceImpl.java",
                'w')
            controllers = FileContent.createServiceImpl(createCodeData, createTableName)
            file.write(controllers)
            file.close()
        #生成Mapper
        path = createCodeData.savePath + "\\CreateAllFileInThePath\\"+pageName+"\\mapper"
        folder = os.path.exists(path)
        if not folder:
            os.mkdir(path)
            file = open(
                createCodeData.savePath + "\\CreateAllFileInThePath\\"+pageName+"\\mapper\\" +createTableName+ "Mapper.java",
                'w')
            controllers = FileContent.createDaoMapper(createCodeData, createTableName)
            file.write(controllers)
            file.close()

        path = createCodeData.savePath + "\\CreateAllFileInThePath\\resources"
        folder = os.path.exists(path)
        if not folder:
            os.mkdir(path)
        path = createCodeData.savePath + "\\CreateAllFileInThePath\\resources\\mybatis"
        folder = os.path.exists(path)
        if not folder:
            os.mkdir(path)
            file = open(
                createCodeData.savePath + "\\CreateAllFileInThePath\\resources\\mybatis\\" +createTableName + "Mapper.xml",
                'w')
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











