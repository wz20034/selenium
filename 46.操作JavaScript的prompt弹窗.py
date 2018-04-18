# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time
import sys

reload(sys)

sys.setdefaultencoding('utf-8')

class OpenTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:\Program Files\Mozilla Firefox\geckodriver")

    def test_HandleConfirm(self):
    	from selenium.common.exceptions import NoAlertPresentException
    	url = "file:///C:/Users/Administrator/Desktop/seleniumTestCase/46test.html"
    	self.driver.get(url)
    	element = self.driver.find_element_by_id("button")
        element.click()
        time.sleep(1)
        alert = self.driver.switch_to.alert
        self.assertEqual(u"这是一个prompt弹出框", alert.text)
        time.sleep(1)
        alert.send_keys(u"光荣之路：要想改变命运，必须每天学习2小时！")
        time.sleep(1)
        # alert.accept()
        alert.dismiss()
    	time.sleep(3)
    			
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()