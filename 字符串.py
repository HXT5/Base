'''
常用方法
join(字符串拼接)
find(查找元素的位置)
count(查找元素的个数)
replace(替换字符)
split(字符串分割)
format(格式化输出)
upper(将字母大写)
lower(将字母转成小写)
'''
person_info="我是小简老师，我喜欢'python30期'，我今天跟你们过节呢！"
# find，正向查找子串sub的最低索引
#参数1，子字符串
#参数2，从参数2位置开始查找
#参数3，到参数3-1位置结束查找
#成功返回位置，失败返回-1
index=person_info.find("喜欢",0,15)
print("1、find:'喜欢'在persion_info的位置是"+str(index))
#count,查找子字符串的个数
#参数1，子字符串
#参数2，从参数2位置开始查找
#参数3，到参数3-1位置结束查找
#成功返回个数，失败返回-1
num=person_info.count("我",0,8)
print("2、count:'我'在persion_info的个数是"+str(num))
#splite,字符串分割
#参数1，分割符
#参数2，分割次数几次，默认分割所有
#成功返回列表，失败返回-1
list=person_info.split("，",2)
print("3、split:'以逗号分割")
print(list[2])
#join,拼接按照分隔符将其拼接起来
#参数1，iterable
#成功返回字符串
str2=";".join(list)
print("4、用';'将分割的list拼接起来",str2)
#replace,替换操作
#参数1，旧的字符
#参数2，新的字符
#参数3，替换次数
#成功返回字符串
str3=person_info.replace("我","I",1)
print("5、将'我'替换为'I'",str3)
#format,格式化
#成功返回字符串
username="zhangsan"
age=7
print("6、format用法：姓名:{0},年龄是{1}岁，今年是{1}岁".format(username,age))
print("我昨天的作业得了{:.2f}分，排名前{:.0%}".format(91.5,0.05))


# 练习
# 1、请找出最中间的字符
str1='Never stop learning!'
index=len(str1)//2
print(str1[index])
#2、截取字符串
print("截取从位置2~位置6的字符串",str1[1:7])
print("截取从位置2~末尾的字符串",str1[1:])
print("截取从开始位置~位置6的字符串",str1[:6])
print("截取完整的字符串",str1[::])
print("从索引3开始，每2个字符串中取一个字符",str1[2::2])
print("截取字符串末尾两个字符",str1[-2:])
print("字符串的倒叙",str1[::-1])


