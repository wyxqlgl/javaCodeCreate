import re
import time
from GetMysqlData import getMysqlData
from tinydb import TinyDB, Query
from CreateCodeData import createCodeData
class createFileDataContent():
    def  createController(self,createCodeData,createTableName):
        result="package "+createCodeData.pathName+".controller;\n"
        oauther=createCodeData.oauther
        description = re.sub("[A-Za-z0-9\!\%\[\]\,\。\ ]", "", createCodeData.tableName).replace("_","").replace("(","").replace(")","")
        result=result+"import java.util.List;\n"
        result=result+"import org.springframework.web.bind.annotation.RestController;\n"
        result=result+"import io.swagger.annotations.*;\n"
        result=result+"import org.springframework.web.bind.annotation.RequestBody;\n"
        result=result+"import org.springframework.web.bind.annotation.PostMapping;\n"
        result=result+"import org.springframework.beans.factory.annotation.Autowired;\n"
        result=result+"import org.springframework.web.bind.annotation.RequestMapping;\n"
        result=result+"/**\n"
        result=result+"  * @author: "+oauther+"\n"
        result=result+"  * @Description "+description+"管理\n"
        result=result+"  * @Datetime "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" \n"
        result=result+"  * @Modified By \n"
        result=result+"  */\n"
        result=result+"@RestController \n"
        result=result+"@Api(value=\""+description+"管理\",tags = {\""+description+"管理\"})\n"
        result=result+"public class "+createTableName+"Controller{\n"
        result=result+"        @Autowired\n"
        result=result+"        "+createTableName+"Service "+self.nameDeal(createTableName)+"Service;\n"
        result=result+"  /** \n    * TODO:  查询数据 \n    * @Param:\n    * @author: "+oauther+"\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"@ApiOperation(\"查询数据\")\n"
        result=result+"@ApiResponses(@ApiResponse(code = 200, message = \"处理成功\",response = "+createTableName+"Vo.class))\n"
        result=result+"@PostMapping(\"/get"+createTableName+"\")\n"
        result=result+"public Object get"+createTableName+"("+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) {\n"
        result=result+"            Object "+self.nameDeal(createTableName)+"Vo="+self.nameDeal(createTableName)+"Service.get"+createTableName+"("+self.nameDeal(createTableName)+"Vo);\n"
        result=result+"            return "+self.nameDeal(createTableName)+"Vo;"
        result=result+"\n}\n\r"
        result=result+"  /** \n    * TODO:  添加数据 \n    * @Param:\n    * @author: "+oauther+"\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"@ApiOperation(\"添加数据\")\n"
        result=result+"@PostMapping(\"/add"+createTableName+"\")\n"
        result=result+"public void add"+createTableName+"(@RequestBody "+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) {\n"
        result=result+"            "+self.nameDeal(createTableName)+"Service.add"+createTableName+"("+self.nameDeal(createTableName)+"Vo);\n"
        result=result+"\n}\n\r"
        result=result+"  /** \n    * TODO:  修改数据 \n    * @Param:\n    * @author: "+oauther+"\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"@ApiOperation(\"修改数据\")\n"
        result=result+"@PostMapping(\"/update"+createTableName+"\")\n"
        result=result+"public void update"+createTableName+"(@RequestBody "+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) {\n"
        result=result+"            "+self.nameDeal(createTableName)+"Service.update"+createTableName+"("+self.nameDeal(createTableName)+"Vo);\n"
        result=result+"\n}\n\r"
        result=result+"  /** \n    * TODO:  删除数据 \n    * @Param:\n    * @author: "+oauther+"\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"@ApiOperation(\"删除数据\")\n"
        result=result+"@PostMapping(\"/del"+createTableName+"\")\n"
        result=result+"public void del"+createTableName+"( String  id) {\n"
        result=result+"            "+self.nameDeal(createTableName)+"Service.del"+createTableName+"(id);\n"
        result=result+"  \n}\n\r"
        result=result+"}\n\r"
        return result
    def createService(self,createCodeData,createTableName):
        oauther=createCodeData.oauther
        result="package "+createCodeData.pathName+".service;\n"
        frame_work = createCodeData.frameWork
        description = re.sub("[A-Za-z0-9\!\%\[\]\,\。\ ]", "", createCodeData.tableName).replace("_","").replace("(","").replace(")","")
        result=result+"import java.util.List;\n"
        result=result+"import "+createCodeData.pathName+".entity."+createTableName+"Vo;\n"
        if frame_work:
            result=result+"import com.baomidou.mybatisplus.extension.service.IService;\n"
        result=result+"/**\n"
        result=result+"  * @author: "+oauther+"\n"
        result=result+"  * @Description "+description+"管理\n"
        result=result+"  * @Datetime "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" \n"
        result=result+"  * @Modified By \n"
        result=result+"  */\n"
        if frame_work:
            result=result+"public interface "+createTableName+"Service extends IService<"+createTableName+"Vo>{\n"
        else:
            result=result+"public interface "+createTableName+"Service{\n"
        result=result+"  /** \n    * TODO:  查询数据 \n    * @Param:\n    * @author: "+oauther+"\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"public Object get"+createTableName+"("+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) ;\n"
        result=result+"  /** \n    * TODO:  添加数据 \n    * @Param:\n    * @author: "+oauther+"\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"public void add"+createTableName+"("+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo);\n"
        result=result+"  /** \n    * TODO:  修改数据 \n    * @Param:\n    * @author: "+oauther+"\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"public void update"+createTableName+"( "+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) ;\n"
        result=result+"  /** \n    * TODO:  删除数据 \n    * @Param:\n    * @author: "+oauther+"\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"public void del"+createTableName+"( String  id) ;\n"
        result=result+"}\n\r"
        return result
    def createServiceImpl(self,createCodeData,createTableName):
        oauther=createCodeData.oauther
        frame_work = createCodeData.frameWork
        result="package "+createCodeData.pathName+".service.impl;\n"
        description = re.sub("[A-Za-z0-9\!\%\[\]\,\。\ ]", "", createCodeData.tableName).replace("_","").replace("(","").replace(")","")
        result=result+"import java.util.List;\n"
        result=result+"import org.springframework.stereotype.Service;\n"
        result=result+"import "+createCodeData.pathName+".mapper."+createTableName+"Mapper;\n"
        result=result+"import "+createCodeData.pathName+".entity."+createTableName+"Vo;\n"
        if frame_work:
            result=result+"import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;\n"
        result=result+"/**\n"
        result=result+"  * @author: "+oauther+"\n"
        result=result+"  * @Description "+description+"管理\n"
        result=result+"  * @Datetime "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" \n"
        result=result+"  * @Modified By \n"
        result=result+"  */\n"
        result=result+"@Service \n"
        if frame_work:
            result=result+"public class "+createTableName+"ServiceImpl extends ServiceImpl<"+createTableName+"Mapper,"+createTableName+"Vo>  implements "+createTableName+"Service{\n"
        else:
            result=result+"public class "+createTableName+"ServiceImpl  implements "+createTableName+"Service{\n"
        result=result+"        @Autowired\n"
        result=result+"        "+createTableName+"Mapper "+self.nameDeal(createTableName)+"Mapper;\n"
        result=result+"  /** \n    * TODO:  查询数据 \n    * @Param:\n    * @author: "+oauther+"\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"    @Override\n"
        result=result+"    public Object get"+createTableName+"("+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) {\n"
        result=result+"           Object "+self.nameDeal(createTableName)+"Vo="+self.nameDeal(createTableName)+"Mapper.get"+createTableName+"("+self.nameDeal(createTableName)+"Vo);\n"
        result=result+"           return "+self.nameDeal(createTableName)+"Vo;"
        result=result+"\n    }\n\r"
        result=result+"   /** \n    * TODO:  添加数据 \n    * @Param:\n    * @author: "+oauther+"\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"    @Override\n"
        result=result+"    public void add"+createTableName+"( "+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) {\n"
        result=result+"           "+self.nameDeal(createTableName)+"Mapper.add"+createTableName+"("+self.nameDeal(createTableName)+"Vo);\n"
        result=result+"\n    }\n\r"
        result=result+"  /** \n    * TODO:  修改数据 \n    * @Param:\n    * @author: "+oauther+"\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"    @Override\n"
        result=result+"    public void update"+createTableName+"( "+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) {\n"
        result=result+"           "+self.nameDeal(createTableName)+"Mapper.update"+createTableName+"("+self.nameDeal(createTableName)+"Vo);\n"
        result=result+"\n    }\n\r"
        result=result+"  /** \n    * TODO:  删除数据 \n    * @Param:\n    * @author: "+oauther+"\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"    @Override\n"
        result=result+"    public void del"+createTableName+"( String  id) {\n"
        result=result+"           "+self.nameDeal(createTableName)+"Mapper.del"+createTableName+"(id);\n"
        result=result+"  \n    }\n\r"
        result=result+"}\n\r"
        return result
    def createDaoMapper(self,createCodeData,createTableName):
        oauther=createCodeData.oauther
        result="package "+createCodeData.pathName+".mapper;\n"
        description = re.sub("[A-Za-z0-9\!\%\[\]\,\。\ ]", "", createCodeData.tableName).replace("_","").replace("(","").replace(")","")
        result=result+"import java.util.List;\n"
        result=result+"import org.apache.ibatis.annotations.Mapper;\n"
        result=result+"/**\n"
        result=result+"  * @author: "+oauther+"\n"
        result=result+"  * @Description "+description+"管理\n"
        result=result+"  * @Datetime "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" \n"
        result=result+"  * @Modified By \n"
        result=result+"  */\n"
        result=result+"@Mapper\n"
        result=result+"public interface "+createTableName+"Mapper{\n"
        result=result+"  /** \n    * TODO:  查询数据 \n    * @Param:\n    * @author: "+oauther+"\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"public Object get"+createTableName+"("+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) ;\n"
        result=result+"  /** \n    * TODO:  添加数据 \n    * @Param:\n    * @author: "+oauther+"\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"public void add"+createTableName+"("+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo);\n"
        result=result+"  /** \n    * TODO:  修改数据 \n    * @Param:\n    * @author: "+oauther+"\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"public void update"+createTableName+"( "+createTableName+"Vo "+self.nameDeal(createTableName)+"Vo) ;\n"
        result=result+"  /** \n    * TODO:  删除数据 \n    * @Param:\n    * @author: "+oauther+"\n    * @Date "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n    */\n"
        result=result+"public void del"+createTableName+"( String  id) ;\n"
        result=result+"}\n\r"
        return result
    def createDaoMapperXml(self,createCodeData,createTableName):
        connection = self.getConnectionData(createCodeData)
        tableName=createCodeData.tableName
        if "(" in tableName:
            nPos=createCodeData.tableName.index("(")
            tableName=createCodeData.tableName[0:nPos]
        result="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        result=result+"<!DOCTYPE mapper PUBLIC \"-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd\">\n"
        result=result+"<mapper namespace=\""+createCodeData.pathName+".mapper."+createTableName+"Mapper\">\n"
        result=result+"    <resultMap id=\""+createTableName+"\" type=\""+createCodeData.pathName+".entity"+createTableName+"Vo\">\n"
        for var in connection:
            columnName=   var.get("columnName")
            result=result+"        <result column=\""+columnName+"\" property=\""+self.dealFiled(columnName)+"\" />\n";
        result=result+"    </resultMap>\n"
        result=result+"    <sql id=\""+createTableName+"Field\">\n"
        for var in connection:
            result=result+"        "+ var.get("columnName")+",\n";
        result=result+"    </sql>\n"
        result=result+"    <select id=\"get"+createTableName+"\" parameterType=\"Map\" resultMap=\""+createTableName+"\">\n"
        result=result+"        select \n"
        result=result+"          <include refid=\""+createTableName+"Field\"/>\n"
        result=result+"        from "+tableName+"\n"
        result=result+"    </select>\n"
        result=result+"    <insert id=\"add"+createTableName+"\">\n"
        result=result+"         insert into"+tableName+"( \n"
        result=result+"          <include refid=\""+createTableName+"Field\"/>\n"
        result=result+"         )values( \n"
        for var in connection:
            columnName=   var.get("columnName")
            result=result+"        #{"+self.dealFiled(columnName)+"},\n";
        result=result+"         )\n"
        result=result+"    </insert>\n"
        result=result+"    <update id=\"update"+createTableName+"\">\n"
        result=result+"          update "+tableName+"set \n"
        for var in connection:
            columnName=   var.get("columnName")
            if columnName !='id':
                result=result+"        "+columnName+"=#{"+self.dealFiled(columnName)+"},\n";
        result=result+"        where id=#{id}\n";
        result=result+"    </update>\n"
        result=result+"    <delete id=\"del"+createTableName+"\">\n"
        result=result+"        delete  from "+tableName+" where  id=#{id}\n";
        result=result+"    </delete>\n"
        result=result+"</mapper>"
        return result
    def createEntity(self,createCodeData,createTableName):
        connection = self.getConnectionData(createCodeData)
        islombok = createCodeData.lombok
        description = re.sub("[A-Za-z0-9\!\%\[\]\,\。\ ]", "", createCodeData.tableName).replace("_","").replace("(","").replace(")","")
        oauther=createCodeData.oauther
        result="/**\n"
        result=result+"  * @author: "+oauther+"\n"
        result=result+"  * @Description "+description+"封装类\n"
        result=result+"  * @Datetime "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" \n"
        result=result+"  * @Modified By \n"
        result=result+"  */\n"
        if islombok:
            result=result+"@Data\n"
        result=result+"public class "+createTableName+"Vo   implements Serializable{\n"
        for var in connection:
            columnName=   var.get("columnName")
            type=   var.get("type")
            columnComment=   var.get("columnComment")
            filed = self.dealFiled(columnName)
            deal_type = self.dealType(type)
            if columnComment is not None and columnComment !='' :
                result=result+"     /** \n       * "+ columnComment +"\n       */\n"
                result=result+"       @ApiModelProperty(value = \""+ columnComment +"\",required = true)\n"
            else:
                result=result+"       @ApiModelProperty(value = \""+ filed +"\",required = true)\n"
            result=result+"       private "+deal_type+" "+filed+";\n\r";
        type=set()
        if islombok !=True:
            for var in connection:
                columnName=   var.get("columnName")
                filed = self.dealFiled(columnName)
                filedName = self.dealFiledName(columnName)
                deal_type = self.dealType(var.get("type"))
                type.add(deal_type)
                result=result+"       public "+deal_type+" get"+filedName+"(){\n";
                result=result+"           return "+filed+";\n";
                result=result+"       }\n";
                result=result+"       public "+deal_type+" set"+filedName+"(){\n";
                result=result+"             return this."+filed+"="+filed+";\n";
                result=result+"       }\n";
        result=result+"}\n\r"
        title="package "+createCodeData.pathName+".entity;\n"
        title=title+"import java.io.Serializable;\n"
        title=title+"import io.swagger.annotations.ApiModelProperty;\n"
        for var in type:
            if var=="Integer":
                title=title+"import java.math.BigDecimal;\n"
            if var=="LocalDateTime":
                title=title+"import java.time.LocalDateTime;\n"
            if var=="Date":
                title=title+"import java.util.Date;\n"
        title=title+"import java.io.Serializable;\n"
        if islombok:
            title=title+"import lombok.Data;\n\r"
        return title+result
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
    def dealFiled(self,dealFiled):
        dealFiled=dealFiled.strip()
        split = dealFiled.split("_",-1)
        dealFiled=""
        count=0
        for ind in split:
            if count !=0:
                dealFiled=dealFiled+ind.capitalize()
            else:
                dealFiled=dealFiled+ind
            count=count+1
        dealFiled = re.sub('\W+', '', dealFiled).replace("_", '')
        pattern = re.compile(r'[\u4e00-\u9fa5]')
        dealFiled = re.sub(pattern,"",dealFiled)
        return dealFiled
    def dealFiledName(self,dealFiled):
        dealFiled=dealFiled.strip()
        split = dealFiled.split("_",-1)
        dealFiled=""
        for ind in split:
                dealFiled=dealFiled+ind.capitalize()
        dealFiled = re.sub('\W+', '', dealFiled).replace("_", '')
        pattern = re.compile(r'[\u4e00-\u9fa5]')
        dealFiled = re.sub(pattern,"",dealFiled)
        return dealFiled
    def dealType(self,type):
        typeMap={
            "bit":"Integer",
            "bool":"Integer",
            "tinyint":"Integer",
            "smallint":"Integer",
            "mediumint":"Integer",
            "int":"Integer",
            "bigint":"Long",
            "float":"Double",
            "double":"Double",
            "decimal":"BigDecimal",
            "char":"String",
            "varchar":"String",
            "tinytext":"String",
            "text":"String",
            "mediumtext":"String",
            "longtext":"String",
            "tinyblob":"String",
            "blob":"String",
            "mediumblob":"String",
            "longblob":"String",
            "date":"Date",
            "datetime":"LocalDateTime",
            "timestamp":"LocalDateTime",
            "time":"LocalDateTime",
            "year":"LocalDateTime"
        }
        type_ = typeMap[type]
        return  type_

