import re
import time
from GetMysqlData import getMysqlData
from tinydb import TinyDB, Query

from CreateCodeData import createCodeData

class createFileDataContent():
    def  createController(self,createCodeData,createTableName):
        result="package "+createCodeData.pathName+".controller;\n"
        description = re.sub("[A-Za-z0-9\!\%\[\]\,\。\ ]", "", createCodeData.tableName).replace("_","").replace("(","").replace(")","")
        result=result+"import java.util.List;\n"
        result=result+"import org.springframework.web.bind.annotation.RestController;\n"
        result=result+"import io.swagger.annotations.*;\n"
        result=result+"import org.springframework.web.bind.annotation.RequestBody;\n"
        result=result+"import org.springframework.web.bind.annotation.PostMapping;\n"
        result=result+"import org.springframework.beans.factory.annotation.Autowired;\n"
        result=result+"import org.springframework.web.bind.annotation.RequestMapping;\n"
        result=result+"/**\n"
        result=result+"  * @author lgl\n"
        result=result+"  * @Description "+description+"管理\n"
        result=result+"  * @Datetime "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" \n"
        result=result+"  * @Modified By \n"
        result=result+"  */\n"
        result=result+"@RestController \n"
        result=result+"@Api(value=\""+description+"管理\",tags = {\""+description+"管理\"})\n"
        result=result+"public class "+createTableName+"Controller{\n"
        result=result+"        @Autowired\n"
        result=result+"        "+createTableName+"Service "+self.nameDeal(createTableName)+"Service;\n"
        result=result+"/** \n    * TODO:  查询数据 \n    * @Param:\n    * @Author: lgl\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"@ApiOperation(\"查询数据\")\n"
        result=result+"@ApiResponses(@ApiResponse(code = 200, message = \"处理成功\",response = "+createTableName+"Vo.class))\n"
        result=result+"@PostMapping(\"/get"+createTableName+"\")\n"
        result=result+"public Object get"+createTableName+"("+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) {\n"
        result=result+"            Object "+self.nameDeal(createTableName)+"Vo="+self.nameDeal(createTableName)+"Service.get"+createTableName+"("+self.nameDeal(createTableName)+"Vo);\n"
        result=result+"            return "+self.nameDeal(createTableName)+"Vo;"
        result=result+"\n}\n\r"
        result=result+"/** \n    * TODO:  添加数据 \n    * @Param:\n    * @Author: lgl\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"@ApiOperation(\"添加数据\")\n"
        result=result+"@PostMapping(\"/add"+createTableName+"\")\n"
        result=result+"public void add"+createTableName+"(@RequestBody "+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) {\n"
        result=result+"            "+self.nameDeal(createTableName)+"Service.add"+createTableName+"("+self.nameDeal(createTableName)+"Vo);\n"
        result=result+"\n}\n\r"
        result=result+"/** \n    * TODO:  修改数据 \n    * @Param:\n    * @Author: lgl\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"@ApiOperation(\"修改数据\")\n"
        result=result+"@PostMapping(\"/update"+createTableName+"\")\n"
        result=result+"public void update"+createTableName+"(@RequestBody "+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) {\n"
        result=result+"            "+self.nameDeal(createTableName)+"Service.update"+createTableName+"("+self.nameDeal(createTableName)+"Vo);\n"
        result=result+"\n}\n\r"
        result=result+"/** \n    * TODO:  删除数据 \n    * @Param:\n    * @Author: lgl\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"@ApiOperation(\"删除数据\")\n"
        result=result+"@PostMapping(\"/del"+createTableName+"\")\n"
        result=result+"public void del"+createTableName+"( String  id) {\n"
        result=result+"            "+self.nameDeal(createTableName)+"Service.del"+createTableName+"(id);\n"
        result=result+"  \n}\n\r"
        result=result+"}\n\r"
        return result
    def createService(self,createCodeData,createTableName):
        result="package "+createCodeData.pathName+".service;\n"
        description = re.sub("[A-Za-z0-9\!\%\[\]\,\。\ ]", "", createCodeData.tableName).replace("_","").replace("(","").replace(")","")
        result=result+"import java.util.List;\n"
        result=result+"/**\n"
        result=result+"  * @author lgl\n"
        result=result+"  * @Description "+description+"管理\n"
        result=result+"  * @Datetime "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" \n"
        result=result+"  * @Modified By \n"
        result=result+"  */\n"
        result=result+"public interface "+createTableName+"Service{\n"
        result=result+"/** \n    * TODO:  查询数据 \n    * @Param:\n    * @Author: lgl\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"public Object get"+createTableName+"("+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) ;\n"
        result=result+"/** \n    * TODO:  添加数据 \n    * @Param:\n    * @Author: lgl\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"public void add"+createTableName+"("+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo);\n"
        result=result+"/** \n    * TODO:  修改数据 \n    * @Param:\n    * @Author: lgl\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"public void update"+createTableName+"( "+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) ;\n"
        result=result+"/** \n    * TODO:  删除数据 \n    * @Param:\n    * @Author: lgl\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"public void del"+createTableName+"( String  id) ;\n"
        result=result+"}\n\r"
        return result
    def createServiceImpl(self,createCodeData,createTableName):
        result="package "+createCodeData.pathName+".service.impl;\n"
        description = re.sub("[A-Za-z0-9\!\%\[\]\,\。\ ]", "", createCodeData.tableName).replace("_","").replace("(","").replace(")","")
        result=result+"import java.util.List;\n"
        result=result+"import org.springframework.stereotype.Service;\n"
        result=result+"/**\n"
        result=result+"  * @author lgl\n"
        result=result+"  * @Description "+description+"管理\n"
        result=result+"  * @Datetime "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" \n"
        result=result+"  * @Modified By \n"
        result=result+"  */\n"
        result=result+"@Service \n"
        result=result+"public class "+createTableName+"ServiceImpl{\n"
        result=result+"        @Autowired\n"
        result=result+"        "+createTableName+"Mapper "+self.nameDeal(createTableName)+"Mapper;\n"
        result=result+"/** \n    * TODO:  查询数据 \n    * @Param:\n    * @Author: lgl\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"@Override\n"
        result=result+"public Object get"+createTableName+"("+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) {\n"
        result=result+"            Object "+self.nameDeal(createTableName)+"Vo="+self.nameDeal(createTableName)+"Mapper.get"+createTableName+"("+self.nameDeal(createTableName)+"Vo);\n"
        result=result+"            return "+self.nameDeal(createTableName)+"Vo;"
        result=result+"\n}\n\r"
        result=result+"/** \n    * TODO:  添加数据 \n    * @Param:\n    * @Author: lgl\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"@Override\n"
        result=result+"public void add"+createTableName+"( "+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) {\n"
        result=result+"            "+self.nameDeal(createTableName)+"Mapper.add"+createTableName+"("+self.nameDeal(createTableName)+"Vo);\n"
        result=result+"\n}\n\r"
        result=result+"/** \n    * TODO:  修改数据 \n    * @Param:\n    * @Author: lgl\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"@Override\n"
        result=result+"public void update"+createTableName+"( "+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) {\n"
        result=result+"            "+self.nameDeal(createTableName)+"Mapper.update"+createTableName+"("+self.nameDeal(createTableName)+"Vo);\n"
        result=result+"\n}\n\r"
        result=result+"/** \n    * TODO:  删除数据 \n    * @Param:\n    * @Author: lgl\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"@Override\n"
        result=result+"public void del"+createTableName+"( String  id) {\n"
        result=result+"            "+self.nameDeal(createTableName)+"Mapper.del"+createTableName+"(id);\n"
        result=result+"  \n}\n\r"
        result=result+"}\n\r"
        return result
    def createDaoMapper(self,createCodeData,createTableName):
        result="package "+createCodeData.pathName+".mapper;\n"
        description = re.sub("[A-Za-z0-9\!\%\[\]\,\。\ ]", "", createCodeData.tableName).replace("_","").replace("(","").replace(")","")
        result=result+"import java.util.List;\n"
        result=result+"import org.apache.ibatis.annotations.Mapper;\n"
        result=result+"/**\n"
        result=result+"  * @author lgl\n"
        result=result+"  * @Description "+description+"管理\n"
        result=result+"  * @Datetime "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" \n"
        result=result+"  * @Modified By \n"
        result=result+"  */\n"
        result=result+"@Mapper\n"
        result=result+"public interface "+createTableName+"Mapper{\n"
        result=result+"/** \n    * TODO:  查询数据 \n    * @Param:\n    * @Author: lgl\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"public Object get"+createTableName+"("+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) ;\n"
        result=result+"/** \n    * TODO:  添加数据 \n    * @Param:\n    * @Author: lgl\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"public void add"+createTableName+"("+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo);\n"
        result=result+"/** \n    * TODO:  修改数据 \n    * @Param:\n    * @Author: lgl\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"public void update"+createTableName+"( "+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) ;\n"
        result=result+"/** \n    * TODO:  删除数据 \n    * @Param:\n    * @Author: lgl\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"public void del"+createTableName+"( String  id) ;\n"
        result=result+"}\n\r"
        return result
    def createDaoMapperXml(self,createCodeData,createTableName):
        connection = self.getConnectionData(createCodeData)
        result="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        result=result+"<!DOCTYPE mapper PUBLIC \"-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd\">\n"
        result=result+"<mapper namespace=\""+createCodeData.pathName+".mapper."+createTableName+"Mapper\">\n"









        result=result+"</mapper>"
        return result
    def createEntity(self,createCodeData,createTableName):
        result="package "+createCodeData.pathName+".entity;\n"
        return result

    def nameDeal(self,name):
        name = name[0].lower()+name[1:]
        return name
    def getConnectionData(self,createCodeData):
        tag=createCodeData.sqlData
        save = TinyDB("AllSaveData.json")
        myCreate = save.table("myConnetion")
        Q = Query()
        data=myCreate.search(Q.name == tag)
        get=getMysqlData(data[0].get("ip"),data[0].get("port"),data[0].get("dbbase"),data[0].get("username"),data[0].get("password"))
        filed = get.getTableFiled(createCodeData.tableName)
        return filed


if __name__ == '__main__':
    createData=createCodeData('mysql','test')
    content = createFileDataContent()
    controller = content.createDaoMapperXml(createData,'Oracle')
    print(controller)

