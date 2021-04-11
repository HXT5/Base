'''
8种定位方式
id：元素id属性
class:元素class属性
name:元素name属性
tag:元素标签名
针对a元素：
link_text:针对a的文本内容-完全匹配
partial_link_text:针对a元素的文本内容-包含

xpath:
    相对定位表达式：
    1、//标签名[@属性名=值]
    2、//标签名[text()=值]    //div[text()='作业']
    3、//标签名[contains(@属性名，值)]  //标签名[contains(text(),值)]
    4、* 标签名或者属性名都可以用*，表示匹配所有//*[contains(@*,值)]

    组合条件
    逻辑：and or
    //标签名[text()=值  and @属性名=值 and contains(@属性名,值)]
    //input[@name='wd' and contains(@id,'kw')]
    层级：
    //祖先节点//要找的节点
    //span[@id='s_kw_wrap']//input
    轴定位：
    元素的兄弟姐妹、子孙、父母
    ancestor:祖先节点包括父
    //img[@class='index-logo-src']/parent::a
    parent:父节点
    preceding:当前元素节点标签之前的所有节点
    preceding-sibling:当前元素节点标签之前的所有兄弟节点
    following:当前元素节点标签之后的所有节点
    following-sibling:当前元素节点标签之后的所有兄弟节点
    使用方法：
    已知的元素/轴名称::标签名称[@属性值=值]




css selector:css选择器

no such element:unable to  locate element
1、在运行结果的页面中copy自己的元素定位，然后通过f12确认元素定位表达式是否有错
2、等待不到位
    可以截图，查看查找时页面的状态 driver.save_screenshot("登录窗口.png")
3、等待
    sleep:强制等待
    implicity_wait：隐式等待
    1、每个会话只调用1次
    2、找元素，命令执行完成
    WebDriverWait(driver,超时时间，查看周期=0.5).until(条件)
    WebDriverWait(driver,超时时间，查看周期=0.5).not_until(条件)
    条件
    presence_of_element_located：元素存在
    visibility_of_element_located：元素可见

'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[text()='登录']").click()
#WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))