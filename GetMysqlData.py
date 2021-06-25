
import MySQLdb
class getMysqlData:
    def __init__(self,ip=None,port=None,dbbase=None,username=None,password=None):
        self.ip=ip
        self.port=port
        self.dbbase=dbbase
        self.username=username
        self.password=password
    def getDataFromMysql(self,mainWind):
        cursor=self.getConnection()
        mainWind.comboBox_2.clear()
        mainWind.comboBox_2.addItem("选择表")
        try:
             sql="SELECT  CONCAT(table_name,(case when table_comment = '' then '' else concat ('(',table_comment,')') end )) table_name FROM    information_schema.tables  WHERE   table_schema='"+self.dbbase+"'";
             cur = cursor.cursor()
             cur.execute(sql)
             for row in cur.fetchall():
                mainWind.comboBox_2.addItem(str(row[0]).replace("('", "").replace("',)", ""))
        except Exception as e: #如果有错，输出错误信息，并回滚，回滚是一种错误处理机制
            cursor.rollback()
        finally:  #最后应该关闭所有的游标和连接
            cursor.close()
    def getTableFiled(self,tableName):
        cursor=self.getConnection()
        tableName = str(tableName)
        result={}
        try:
            if tableName !='选择表' and tableName !='':
                nPos=tableName.index("(")
                tableName=tableName[0:nPos]
                sql="select COLUMN_NAME,COLUMN_COMMENT,DATA_TYPE from information_schema.COLUMNS where table_name = '"+tableName+"  ' and table_schema='"+self.dbbase+"'";
                cur = cursor.cursor()
                cur.execute(sql)
                fetchall = cur.fetchall()
                for row in fetchall:
                    name=row[0]
                    value=row[1]
                    if name!='':
                        result[name]=value
        except Exception as e: #如果有错，输出错误信息，并回滚，回滚是一种错误处理机制
            cursor.rollback()
        finally:  #最后应该关闭所有的游标和连接
            cursor.close()
        return result
    def getConnection(self):
        db = MySQLdb.connect(
            host=self.ip,  # 主机名
            user=self.username,     # 用户名
            passwd=self.password, # 密码
            db=self.dbbase,
            port=int(self.port),
            charset='utf8')
        return db



