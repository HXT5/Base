'''
1、什么是异常
2、python中的异常类型
3、遇到异常时的异常分析
4、异常捕获
5、断言异常

try:
    可能会出错的代码
except:(如果出错了，进入except)
    代码报错之后会执行的代码
else:
    try里面代码没报错的时候，会执行的代码
finally:
    无论是否出现异常，一定会执行的代码
'''

try:
    fs=open("./io.txt","r",encoding="utf-8")
    print(fs.read())
except FileNotFoundError as f:
    print(f)
    print("文件不存在")
except KeyError:
    print("key错误")
except:
    print("ERROR")