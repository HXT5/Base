'''
logging模块
日志收集器=>渠道（Handle）=>日志格式（Fomatter）
0、日志名字
1、日志级别(Level)：DEBUG、INFO、WARNING、ERROR、CRITICAL(FATAL)
2、输出渠道（Handle）：控制台(StreamHandle)、文件(FileHandle)
3、日志内容（Format）：时间-哪个文件-哪行代码-输出内容

logging模块，默认的root日志收集器，默认的输出级别：WARNING
第一步：
创建日志收集器logging.getLogger("collect")
第二步：
给日志收集器设置日志级别：logger.setLevel(logging.INFO)
第三步：
给日志收集器，创建一个输出渠道。handle1=logging.StreamHandler()
第四步：
给渠道，设置一个日志输出内容的格式
第五步：
将设置的格式，绑定到渠道当中，将格式与渠道关联起来
第六步：
将设置好的渠道，添加到日志收集器上
'''
import logging
# logging.info("日志输出")
# logging.warning("日志")
logger=logging.getLogger("collection")
#设置日志输出级别
logger.setLevel(logging.INFO)
#设置日志输出在哪个渠道
handle1=logging.StreamHandler()
#设置渠道自己的输出级别
handle1.setLevel(logging.ERROR)
#设置渠道的输出内容格式
fmt='%(asctime)s-%(name)s-%(levelname)s-%(filename)s-%(lineno)d行:%(message)s '
fomatter=logging.Formatter(fmt)
#将日志格式绑定到渠道当中
handle1.setFormatter(fomatter)
#将设置好的渠道，添加到日志收集器上
logger.addHandler(handle1)
#添加fileHandler
handle2=logging.FileHandler("my_py30.log",encoding="utf-8")
handle2.setFormatter(fomatter)
logger.addHandler(handle2)
logger.info("收集器")
logger.error("收集器")






