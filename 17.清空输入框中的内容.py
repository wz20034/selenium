# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_clearInputBoxText(self):
		url = "http://www.baidu.com"
		self.driver.get(url)
		input1 = self.driver.find_element_by_id("kw")
		input1.send_keys(u"光荣之路自动化测试")
		time.sleep(3)
		input1.clear()
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()