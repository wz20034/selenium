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

    def test_HandleAlert(self):
    	from selenium.common.exceptions import NoAlertPresentException

    	url = "file:///C:/Users/Administrator/Desktop/seleniumTestCase/44test.html"
    	self.driver.get(url)
    	button = self.driver.find_element_by_id("button")
    	button.click()
    	try:
    		alert = self.driver.switch_to_alert()
    		time.sleep(2)
    		self.assertEqual(alert.text, u"这是一个alert弹出框")
    		alert.accept()
    	except NoAlertPresentException, e:
    		self.fail("尝试操作的alert框未被找到")
    		print e
    	time.sleep(3)
    			
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()