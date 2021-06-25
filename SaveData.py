from tinydb import TinyDB
class saveData():
    def __init__(self,createCodeData):
        self.sqlPath = createCodeData.sqlPath  # 保存路径
        self.tableName = createCodeData.tableName  # 已经存在的表
        self.pathName = createCodeData.pathName  # 生成的文件名称
        self.savePath = createCodeData.savePath  # 保存到那个路径
        self.frameWork = createCodeData.frameWork  # 选择的框架
        self.isEnum = createCodeData.isEnum  # 是否枚举
        self.isCatch = createCodeData.isCatch  # 是否用缓存
        self.lombok = createCodeData.lombok  # 是否用lombok插件
        self.dataBaseUrl = createCodeData.dataBaseUrl  # 数据源url
        self.dataBasePort = createCodeData.dataBasePort  # 数据源port
        self.dataBaseUser = createCodeData.dataBaseUser  # 数据源用户名
        self.dataBasePwd = createCodeData.dataBasePwd  # 数据源密码
    def saveAllData(self):
        save=TinyDB("AllSaveData.json")
        myCreate=save.table("myCreate")
        myCreate.insert({'sqlPath':self.sqlPath,
                         'tableName':self.tableName,
                         'pathName':self.pathName,
                         'savePath':self.savePath,
                         'frameWork':self.frameWork,
                         'isEnum':self.isEnum,
                         'isCatch':self.isCatch,
                         'lombok':self.lombok,
                         })
