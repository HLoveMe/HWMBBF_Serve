# HWMBBF_Serve
该服务器版本是基于Django 1.8 版本 并且只是为 ( https://github.com/HLoveMe/HMBBF ) 提供了基本数据服务

注意: HMBBF 如果可以正常运转 您将不需要使用该项目

操作：

  1：环境配置
  
    python3
    
    Django 1.8
    
    pymysql(mysql链接库)
    
    MYSQL数据库
    
  2:数据导入(该数据只是包含部分数据)
  
    下载文件中的MYSQL_DATA为MYSQL数据库导出文件
    
  3:工程配置
  
    HWMBBF_serve项目  下 HWHMBBF/setting.py   修改数据库连接配置
    
    打开HMBBF项目目录 (www/js/customServices.js 修改dataService服务的 mainUrl 属性)
    
    
