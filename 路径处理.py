'''
1、本地路径处理
    （1）获取文件绝对路径
    （2）获取文件所在目录
    （3）魔法变量：__file__、__name__
熟记os.path.dirname和os.path.join
os.path.dirname() 返回文件/目录所在路径
os.path.join(a,b) 连接两个部分的路径，组成一个完整的路径
os.path.abspath() 获取绝对路径
=========================================================
os.getcwd() 显示当前的工作路径
os.chdir()切换工作路径
os.mkdir() 在某个目录下创建一个新目录
os.rmdir() 删掉一个目录
os.listdir() 获取当前路径下的目录列表，返回列表格式数
os.path.isdir()判断当前文件是否是目录
os.path.isfile()判断当前文件是否是文件
'''
import os
'''
获取当前文件的绝对路径
'''
path1=os.path.abspath("io.txt")
print("io.txt的绝对路径是",path1)
'''
返回文件/目录所在路径
'''
path2=os.path.dirname(path1)
print("io.txt所在目录是",path2)

'''
拼接路径，如得到列表.py的绝对路径
'''
path3=os.path.join(path2,"列表.py")
print("拼接路径",path3)

basedir=os.path.dirname(os.path.abspath("io.txt"))
print("连写获取项目根目录",basedir)

'''
魔法变量
__file__:代表当前文件名
__name__:所在模块（文件）的模块名
'''
path4=os.path.abspath(__file__)
print("使用__file__代表当前文件名",path4)
print("所在模块（文件）的模块名",__name__)

if __name__ == '__main__':
    print("运行")





