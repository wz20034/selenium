# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_getTitle(self):
		url = "http://www.baidu.com"
		self.driver.get(url)
		title = self.driver.title
		print "当前网页的title属性为：", title 
		self.assertEqual(title, u"百度一下，你就知道", "页面title属性值错误!")
		time.sleep(5) 

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()