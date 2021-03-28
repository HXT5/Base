import unittest
'''
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
'''
def login_check(username=None,password=None):
    if username!=None and password!=None:
        if username=="python" and password=="123456":
            return {"code":0,"msg":"登录成功"}
        else:
            return {"code":1,"msg":"账号或密码不正确"}
    else:
        return {"code":1,"msg":"所有的参数不能为空"}
class TestLogin(unittest.TestCase):
    def test_login_ok(self):
        # 1、测试数据 2、测试步骤
        res=login_check("python","123456")
        # 3、断言：预期结果与实际结果的比对
        self.assertEqual(res,{"code":0,"msg":"登录成功"})
    def test_login_wrong_password(self):
        pass
    def test_logn_wrong_user(self):
        pass
    def test_login_no_passwd(self):
        pass
    def test_login_no_user(self):
        pass