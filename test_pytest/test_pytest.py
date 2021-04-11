'''
unittest和pytest
共同点
1、测试框架-通过python代码来写测试用例，收集用例，运行用例，生成报告

unitest
    写用例---T继承estCase
          ---前置后置
                setup/teardown  setupClass,tearDownClass
          ----断言
                self.assertXXXX()
    收集用例和运行用例---TestLoader.discover(目录)
               收集到套件当中，run方法去执行

    生成报告---HtmlTestRunner
    HtmlTestRunner、BeautifulReport
pytest
    写用例---函数/类里面的方法--用例名称必须以test_开头。如果用例在类中，类名必须以Test开头
          ---前置后置
          ----方案1：沿用了unittest的风格
                1、用例级别：setup,teardown
                2、类级别：setup_class teardown_class
                3、模块级别：setup_module teardown_module
           ----方案2：fixture
              先定义再调用
               1、函数实现的，函数名称不固定----如何区分前置后置？
               @pytest.fixture
                def fix():
                    pass
               2、前置操作和后置操作，写在一个函数里----如何区分前置后置
               @pytest.fixture
                def fix():
                    前置代码
                    yeild  #分割线
                    后置代码
                3、4个作用域，测试函数（function）,测试类（class）,测试模块文件（module）,测试会话（session）
                    @pytest.fixture（scope=function（默认值）/class/module/session）
                    def fix():
                         前置代码
                        yeild  #分割线
                        后置代码
                4、不跟测试类/测试函数放在一起
                5、前置操作得到的一些数据，如何传递测试用例
                 yeild 返回值
                 在测试用例当中，以fixture名作为用例参数。用例参数接收返回值
                6、共享机制：conftest.py
            调用
                fixtures.函数名 哪需要哪调
                @pytest.mark.usefixtures("fixture的函数名称")
                测试类/测试函数

           ----断言
               assert 表达式
    收集用例和运行用例
         不需要写任何代码去收集用例-自动收集/发现用例的方式
         执行用例 pytest [参数]
         方式一：pytest -s -v 控制台显示详细的用例执行情况
         方拾二：pytest文件：pytest.main([命令行参数])
    如何自动收集用例的？
    1、目录-从哪个目录下开始搜索用例
       rootdir:pytest命令在哪个目录下执行，就以哪个目录为rootdir
    2、文件名-命名符合test_*.py或者*test.py条件的文件名，它里边是会有用例
    3、函数/类下方法-函数以test_开头
                    以Test开头（不含__init__）的类下的test_开头方法
    执行顺序
        1、文件名：ASCII
        2、文件内部：按代码先后顺序
    生成测试报告
        html-插件 pip install pytest-html  --html=html的路径
        allure-插件 pip install allure-pytest
        allure命令行工具下载https://docs.qameta.io/allure/
        https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.9.0/

        allure serve 生成allure文件的目录   cd test_pytest    allure serve allure_dir

    pytest-参数化
    @pytest.mark.parametrize("参数名",列表数据)
    @pytest.mark.parametrize("a,b,c",[(1,3,4),(5,8,9),(22,33,55,88,99)])
    def test_add(a,b,c)
        res=a+b
        assertres==c

    打标记
    对用例打标计，运行的时候，只运行打标记的用例
    1、得先注册标记名
    pytest.ini
    [pytest]
        markers=
            mark1：说明只能是英文
            mark2
            mark3
    2、给测试用例/测试类打标记
    @pytest.mark.已注册的标记
    3、运行时设置只运行标记的用例
    -m 标记名


    失败重运行机制：
        用例失败的情况下，可以重运行用例
        pip install pytest-rerunfailures
        使用：
            pytest --reruns 重试次数
            pytest --reruns 2 --reruns-delay 5
            失败的用例可以重新运行2次，第一次和第二次的间隔时间为5秒


'''
import pytest
def test_abc():
    print("abc")
class TestABC:
    def setup_class(self):
        print("类前置")
    def setup(self):
        print("用例前置")
    def test_abc2(self):
        print("abc2")
    def test_abc3(self):
        print("abc3")
    def teardown(self):
        print("用例后置")
    @pytest.mark.parametrize("a",[(1,3,4),(5,8,9),(22,33,55)])
    def test_add(self,a):
        print(a)

    def teardown_class(self):
        print("类后置")
if __name__ == '__main__':
    pytest.main(["-s","-v","--alluredir=allure_dir","--html=report.html"])