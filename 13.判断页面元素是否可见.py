# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time
import sys

reload(sys)

sys.setdefaultencoding('utf-8')

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_getWebElementAttribute(self):
		url = "http://www.sogou.com"
		self.driver.get(url)
		searchBox = self.driver.find_element_by_id("query")
		print searchBox.get_attribute("name")
		searchBox.send_keys(u"测试工程师指定的输入内容")
		print searchBox.get_attribute("value")

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()