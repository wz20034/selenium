# -*- coding:utf-8 -*-  
from selenium import webdriver
import unittest
import traceback
import time

def addAttribute(driver, elementObj, attributeName, value):
    driver.execute_script("arguments[0].%s = arguments[1]" %attributeName, elementObj, value)

def setAttribute(driver, elementObj, attributeName, value):
    driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2])", elementObj, attributeName, value)

def getAttribute(elementObj, attributeName):
    return elementObj.get_attribute(attributeName)

def removeAttribute(driver, elementObj, attributeName):
    driver.execute_script("arguments[0].removeAttribute(arguments[1]", elementObj, attributeName)

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:\Program Files\Mozilla Firefox\geckodriver")

    def test_scroll(self):
        url = "file:///C:/Users/Administrator/Desktop/seleniumTestCase/53test.html"
        self.driver.get(url)
        element = self.driver.find_element_by_xpath("//input")
        addAttribute(self.driver, element, "name", "search")
        print u'添加的新属性值%s = "%s"' %("name", getAttribute(element, "name"))
        setAttribute(self.driver, element, "value", u"这是更改后的内容")
        print u"更改后文本框的内容：", getAttribute(element, "value")        
        setAttribute(self.driver, element, "size", 20)
        print u"更改后文本框标签中的size属性值：", getAttribute(element, "size")
        # removeAttribute(self.driver, element, "value")
        # print u"删除value属性值后value的属性值：", getAttribute(element, "value")
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()