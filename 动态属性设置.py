'''
类定义之后，动态的给类/对象添加/删除属性
动态设置属性：hasattr,getattr,setattr,delattr
不确定类的属性名和属性值是什么歌
从其他地方获取到后，动态给类添加属性和值
'''
class People:
    def __init__(self,name):
        self.name=name
p=People("xj")
ss=p
'''
hasattr
'''
res=hasattr(People,"name")
print(res)#类没有name
res=hasattr(p,"name")
print(res)#实例对象有name
'''
getattr获取属性
'''
# attr=getattr(People,"name")报错，类没有该属性
# # print(attr)
attr=getattr(p,"name")
print(attr)
'''
setattr设置属性
如果属性存在，修改属性，如果不存在，添加属性
'''
setattr(People,"kind","黄种人")
print(People.kind)

print(isinstance(p,People))#P是People的对象
print(ss is p)