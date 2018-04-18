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

	def test_getPageSource(self):
		url = "http://www.sogou.com"
		self.driver.get(url)
		pageSource = self.driver.page_source
		print pageSource
		self.assertTrue(u"新闻" in pageSource, "页面源码中未找到'新闻'关键字")
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()