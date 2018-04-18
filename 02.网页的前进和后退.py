# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_visitRecentURL(self):
		firstVisitURL = "http://www.sogou.com"
		secondVisitURL = "http://www.baidu.com"
		self.driver.get(firstVisitURL)
		time.sleep(3)
		self.driver.get(secondVisitURL)
		time.sleep(3)
		#回退上个页面
		self.driver.back()
		time.sleep(3)
		#前进到下个页面
		self.driver.forward()
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()