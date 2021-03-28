'''
类：同一类事物的  抽象描述
对象：符合类描述的  具体存在
类属性：直接在类当中定义的，不在任何的实例方法当中
类行为：函数加上@classmethod 参数默认为cls，cls表示类本身，可以通过cls访问类的属性，但是类不能访问实例属性
实例属性：self.属性名
实例方法：参数第一个就是self,实例都是可以访问类的属性，类方法的
静态方法：使用@staticmethod修饰，与类无任何关联，就是一个普通函数，参数无self,cls，类/实例均可访问
'''
class Dog:
    kind="dog" #类属性，不论类的哪一个对象，它的kind全都是一样的
    def __init__(self,name,kind,age):
        self.dog_name=name #实例属性
        self.dog_kind=kind
        self.dog_age=age
    @classmethod #声明为类方法
    def set_kind(cls):#cls代表类
        print(cls.kind)
    def bark(self): #实例方法
        print("bark")
Dog.set_kind()

'''
继承语法：class 子类（父类）
私有化：父类当中以__开头的属性/行为，子类都不可以继承，仅父类内部可用
类定义时，_开头的属性/方法，父类内部/子类内部都可以用（尽量不调用）
super:子类中：super().方法名()--调用父类同名方法

'''
class Base(object):
    def __init__(self,name):
        print("初始化Base类！")
        self.__name=name
    def eat(self):
        print("吃")
        print(self.__name)
class Cat(Base):
    def __init__(self,name,sex):
        super().__init__(name)
        print("初始化Cat类")
        self.name=name
        self.sex=sex
    def climb(self):
        #print(self.__name)#父类私有化的属性，子类不能用
        self.eat()
    def eat(self):
        super().eat()#与父类同名，调用父类方法用super().方法
        print("喝")

c=Cat(1000)
c.eat()



