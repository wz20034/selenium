# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_captureScreenInCurrentWindow(self):
		url = "http://www.sogou.com"
		self.driver.get(url)
		try:
			result = self.driver.get_screenshot_as_file(r"C:/Users/Administrator/Desktop/seleniumTestCase/28.png")
			print result
		except IOError, e:
			print e
		time.sleep(4)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()