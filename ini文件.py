'''
.ini
[section]
option=value
option=value
'''
from configparser import ConfigParser
#1、实例化
conf=ConfigParser()
#2、读取配置文件
conf.read("./base/test_case/conf.ini",encoding="utf-8")
#3、读取某一项配置：get,全部都是字符串
#getboolean,getint,getfloat
name=conf.get("log","name")
level=conf.get("log","level")
file_name=conf.get("log","file_name")

#获取当前所有section
conf.sections()
#获取所有的选项
conf.options("log")

'''
写入操作
'''
conf.set("log","file_name","test1.log")
#新增session
conf.add_section("mysql")
conf.write(open("./base/test_case/conf.ini","w",encoding="utf-8"))






