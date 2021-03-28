#args是元组
#**kwargs是字典
def getnum(num,*args,**kwargs):
    print("args:")
    print(args)
    print("*args:")
    print(*args)
    print("kwargs:")
    print(kwargs)
    print("*kwargs:")
    print(*kwargs)
    # print("**kwargs:")
    # print(**kwargs)
#getnum(1,True,"a","b",a=1,b=2)

#*传递参数时可以对元组/列表拆包
#**传递参数时可以对字典拆包
num_list=[100,200,300,400]
def getlist(a,b,c,d):
    sum=a+b+c+d
    print(sum)
getlist(*num_list)
dict={"a":1,"b":2}
def getdict(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)
getdict(**dict)
