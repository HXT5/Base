'''
1、放的都是fixture
2、fixtures可以对外共享
3、共享范围
    当前conftest.py所在目录下的（子孙目录）所有用例
4、conftest.py是可以创建多个，在不同的包下，可以层级创建的
5、优先级：就近原则
    发现fixture：用例自己的模块-》用例所在目录下的conftest.py->目录的父级目录下的conftest.py
6、嵌套方式
    什么时候嵌套？一个fixture，想完全使用另外一个fixture，并在人家的基础上新增一些代码
    怎么嵌套
    @pytest.fixture
    def fix1()
       pass
    @pytest.fixture
    def fix2(fix1)
        #新增的代码
       pass
    嵌套后的执行顺序
       fix1的前置
       fix2的前置
       fix2的后置
       fix1的后置
'''
import pytest
@pytest.fixture()
def con():
    print("conftest中的fixture")