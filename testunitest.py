import unittest
import ddt
import os
import logging
'''
表达用例=》收集用例=》执行用例=》生成报告
4个核心概念：
用例编写TestCase
用例套件TestSuite-容器，放用例
用例收集TestLoader-收集用例
生成报告TextTestRunner

定义测试类，继承unittest.TestCase
在测试类当中，以test_开头，定义测试函数
每一个test_开头的函数，就是一个测试用例
编写用例：
    1、测试数据
    2、测试步骤
    3、断言：预期结果与实际结果的比对
    assertEqual(a,b) a==b
    assertNotEqual(a,b) a!=b
    assertTrue(x)  bool(x) is True
    assertFalse(x)  bool(x) is False
    assertis(a,b)   a is b
    assertisNot(a,b)  a is not b
    assertin(a,b)  a in b
    assertNotin(a,b) a not in b
    4、前置后置（fixture）
    setup,类下面的每一个用例在执行之前，会执行setup
    teardown,类下面在每一个用例执行后会执行
收集用例：
TestLoader-discover(搜索目录)
执行用例：
引入ddt:
    1、在测试类名的上面，用@ddt.ddt
    2、在测试函数上面，用@ddt.data(*列表)
    
'''
Base_dir=os.path.dirname(os.path.abspath(__file__))
datas=[
    {"username":"python","password":"123456","res":{"code":0,"msg":"登录成功"}},
    {"username":"python","password":"1234567","res":{"code":1,"msg":"账号或密码不正确"}},
    {"username":"python1","password":"123456","res":{"code": 1, "msg": "账号或密码不正确"}},
    {"username":"python","password":None,"res":{"code":1,"msg":"所有的参数不能为空"}},
    {"username":None,"password":"123456","res":{"code": 1, "msg": "所有的参数不能为空"}},
]
def login_check(username=None,password=None):
    if username!=None and password!=None:
        if username=="python" and password=="123456":
            return {"code":0,"msg":"登录成功"}
        else:
            return {"code":1,"msg":"账号或密码不正确"}
    else:
        return {"code":1,"msg":"所有的参数不能为空"}

#编写用例
@ddt.ddt
class TestLogin(unittest.TestCase):
    # def setUp(self) -> None:
    #     print("=====单个用例开始执行=====")
    # def tearDown(self) -> None:
    #     print("=====单个用例执行结束=====")
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("======所有用例开始执行=====")
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("=====所有用例执行结束=====")
    @ddt.data(*datas)
    def test_login(self,case):
        print(case)
        res=login_check(case["username"],case["password"])
        self.assertEqual(res,case["res"])
    # def test_login_ok(self):
    #     # 1、测试数据 2、测试步骤
    #     res=login_check("python","123456")
    #     # 3、断言：预期结果与实际结果的比对
    #     self.assertEqual(res,{"code":0,"msg":"登录成功"})
    # def test_login_wrong_password(self):
    #     # 1、测试数据 2、测试步骤
    #     res = login_check("python", "1234567")
    #     # 3、断言：预期结果与实际结果的比对
    #     self.assertEqual(res, {"code":1,"msg":"账号或密码不正确"})
    # def test_logn_wrong_user(self):
    #     # 1、测试数据 2、测试步骤
    #     res = login_check("python1", "123456")
    #     # 3、断言：预期结果与实际结果的比对
    #     self.assertEqual(res, {"code": 1, "msg": "账号或密码不正确"})
    # def test_login_no_passwd(self):
    #     # 1、测试数据 2、测试步骤
    #     res = login_check("python")
    #     # 3、断言：预期结果与实际结果的比对
    #     self.assertEqual(res, {"code":1,"msg":"所有的参数不能为空"})
    # def test_login_no_user(self):
    #     # 1、测试数据 2、测试步骤
    #     res = login_check("123456")
    #     # 3、断言：预期结果与实际结果的比对
    #     self.assertEqual(res, {"code": 1, "msg": "所有的参数不能为空"})
#实例化测试套件
# s=unittest.TestSuite()
#添加1个用例
#s.addTest(TestLogin("test_login_ok"))
#添加多个用例
#s.addTests([TestLogin("test_login_ok"),TestLogin("test_login_wrong_password")])
'''
收集用例
Testloader
可以通过类名、模块名、目录三种方式去收集用例
方法一：目录（常用）
unittest.TestLoader().discover(搜索目录) 默认在test*.py中搜索用例
方法二：类名（了解）
unittest.TestLoader().loadTestsFromTestCase(测试类名) 测试类名不需要加引号
方法三：模块名（了解）
unittest.TestLoader().loadTestsFromModule(模块名) 模块名不需要加引号

'''
#从目录下开始，搜索所有的测试用例
#1、指定搜索目录
#2、文件过滤规则，以文件名匹配，test*.py
#3、在文件当中过滤:继承了unittest.TestCase类的测试类，类当中以test_开头的函数
# suite=unittest.TestLoader().discover(r"C:\Users\HXT\Desktop\Base")
suite=unittest.TestLoader().discover(Base_dir)
# print(s)
'''
执行用例+测试报告
TextTestRunner,运行测试用例，结果以text呈现
HtmlTestRunner,运行测试用例，结果以html呈现
'''
# with open('test_result.txt','w') as f:
# #     runner=unittest.TextTestRunner(f)
# #     runner.run(suite)
from HTMLTestRunner import HTMLTestRunner
with open("./index.html","wb") as f:
    HTMLTestRunner(f).run(suite)
