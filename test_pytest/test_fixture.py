import pytest
@pytest.fixture()
def ini():
    print("作用域为测试函数前置代码级别")
    yield  True
    print("作用域为测试函数后置代码级别")
@pytest.fixture(scope="class")
def class_fix():
    print("作用域为测试类前置代码级别")
    yield
    print("作用域为测试类后置代码级别")


def test_abc():
    print("===函数用例===")
@pytest.mark.usefixtures("class_fix")
class TestDay:
    @pytest.mark.usefixtures("ini")
    @pytest.mark.usefixtures("con")
    @pytest.mark.smoke
    def test_new1(self,ini):
        print(ini)
        print("===类下的用例1")
    def test_new2(self):
        print("===类下的用例2")
    def test_new3(self):
        print("===类下的用例3")
    @pytest.mark.parametrize("a",[(1,3,4),(5,8,9),(22,33,55)])
    def test_add(self,a):
        print(a)
    @pytest.mark.parametrize("a,b,c",[(1,3,4),(5,8,9),(22,33,55)])
    def test_add1(self,a,b,c):
        print(a)
    @pytest.mark.parametrize("x",[0,1])
    @pytest.mark.parametrize("y",[2,3])
    @pytest.mark.smoke
    @pytest.mark.demo
    def test_foo(self,x,y):
        print(x,y)
if __name__ == '__main__':
    pytest.main(["-s","-v","-m","smoke and demo"])