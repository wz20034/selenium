# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_assertKeyWord(self):
		url = "http://www.baidu.com"
		self.driver.get(url)
		self.driver.find_element_by_id("kw").send_keys(u"光荣之路自动化测试")
		self.driver.find_element_by_id("su").click()
		time.sleep(4)
		assert u"首页--光荣之路" in self.driver.page_source, u"页面源码不存在该关键字!"


	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()