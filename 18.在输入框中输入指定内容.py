# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_sendTextToInputBoxText(self):
		url = r"file:///C:/Users/Administrator/Desktop/seleniumTestCase/18test.html"
		self.driver.get(url)
		input_1 = self.driver.find_element_by_id("text")
		input_1.clear()
		input_1.send_keys(u"我是输入的文本内容")
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()