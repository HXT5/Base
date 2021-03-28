'''
文件操作
1、文件的打开操作（打开模式，编码格式）
2、文件的读、写操作
3、文件的关闭操作
4、with as 应用
r 只读
    1、文件一定要存在，否则报错
    2、默认为只读模式
w 只写
    1、若文件不存在，会自动创建
    2、文件所在的目录一定要存在，否则报错
    3、会覆盖原有内容
a 追加
    1、若文件不存在，会自动创建
    2、文件所在的目录一定要存在，否则报错
    3、若文件存在，则直接在文件末尾继续追加内容
rb 只读
    二进制的方式写、其它一样，通常用于打开图片
wb 只写
    二进制的方式读、其它一样，通常用于打开图片
ab 追加
    二进制的方式追加、其它一样，通常用于打开图片
'''
#读
#read 读取文件的所有数据，默认从头开始，读取出来为字符串
#readline()读取一行数据
#readlines()按行读取所有数据，结果为列表，一行为一个成员
# fs=open("./io.txt","r",encoding="utf-8")
# s=fs.read()
#s=fs.readline()
# s=fs.readlines()
# print(s)
#写
#文件写入数据时，不会自动换行，需要在数据当中，加入换行符\n
#write(数据) 写入数据
#writelines(列表) 写入列表当中的每个成员，列表里是字符串
# fs=open("./io.txt","w",encoding="utf-8")
# fs.write("你好")
# fs.close()
#追加
# fs=open("./io.txt","a",encoding="utf-8")
# fs.write("\n追加")
# fs.close()
#可读可写
# r+ 可读可追加
# w+先写后读
# fs=open("./io.txt","r+",encoding="utf-8")
# s=fs.read()
# print(s)
# fs.write("hello")
#使用with的好处是会启动文件的上下文管理器，不需要关闭文件，会自动关闭文件
# with open("./io.txt","r") as file:
#     print(file.read())

with open("./io.txt","w") as file:
    file.write("name,age,gender,hobby,motto\n")
person_info=[{"name":"yuze","age":"18","gender":"男","hobby":"看球","moto":"success"},{"name":"zhangsan","age":"18","gender":"男","hobby":"watchTV","moto":"success"}]
with open("./io.txt","a",encoding="utf-8") as file:
    i=0
    while(i<len(person_info)):
        str = ""
        list1=list(person_info[i].values())
        str=",".join(list1)
        file.write(str+"\n")
        i=i+1






