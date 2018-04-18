# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_window_size(self):
		url = "http://www.baidu.com"
		self.driver.get(url)
		sizeDict = self.driver.get_window_size()
		print "当前浏览器窗口的宽：", sizeDict['width']
		print "当前浏览器窗口的高：", sizeDict['height']
		time.sleep(3)
		self.driver.set_window_size(width = 200, height = 400, windowHandle = 'current')
		print self.driver.get_window_size(windowHandle = 'current')
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()