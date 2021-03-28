'''
字典
'''
#添加
dict={"a":1,"b":2,"c":3}
dict1={"d":4}
dict.update(dict1)
print("1、将字典2的数据更新到字典1中")
print(dict)
#del,删除字典某个key值
del dict["d"]
print("2、del:删除字典key是d的值")
print(dict)
#pop,删除字典某个key:value
dict.pop("b")
print("3、pop:删除字典某个key:value")
print(dict)
#clear,清空列表
# dict.clear()
# print("4、clear:清空字典")
# print(dict)
key=dict.keys()
print("5、获得所有key")
print(key)
value=dict.values()
print("6、获得所有value")
print(value)