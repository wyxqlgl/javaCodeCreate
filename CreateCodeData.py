
class createCodeData():
    def __init__(self,tableName=None,pathName=None,savePath=None,frameWork=None,lombok=None,isJPA=None,isCreateFile=None,sqlData=None,oauther=None):
        self.tableName=tableName #选择的表
        self.pathName=pathName #生成的文件名称
        self.savePath=savePath #保存到那个路径
        self.frameWork=frameWork #是否选择mybatisplus
        self.lombok=lombok #是否用lombok插件
        self.isJPA=isJPA #是否用jpa
        self.isCreateFile=isCreateFile #是否用只生成文件
        self.sqlData=sqlData #选中数据源
        self.oauther=oauther #开发代码的人

