'''
列表
增
append,insert,extend
删
del,remove,pop,clear
改
查
'''
list=[1,2,5]
#append,追加在末尾
list.append(6)
print("1、append:在列表末尾追加6")
print(list)
#insert，在固定位置插入
list.insert(2,4)
print("2、insert:在列表位置2追加4")
print(list)
#extend,将列表2追加到列表1
list1=[7,8]
list.extend(list1)
print("3、extend:将列表2追加到列表1")
print(list)
#del,删除列表中某个索引的数据
del list[0]
print("4、del:删除列表的第0个元素")
print(list)
#remove，删除列表中第一次出现的指定数据
list.remove(2)
print("5、remove:删除列表2")
print(list)
#pop,删除列表末尾数据
list.pop()
print("6、pop:删除列表最后一个元素")
print(list)
#clear,清空列表
# list.clear()
# print("7、clear:清空列表")
# print(list)
#排序
list.sort()
print("7、列表的正序")
print(list)
list.sort(reverse=True)
print("8、列表的倒序")
print(list)
list.reverse()
print("9、列表的反转")
print(list)
