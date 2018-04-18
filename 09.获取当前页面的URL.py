# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_getCurrentPageUrl(self):
		url = "http://www.sogou.com"
		self.driver.get(url)
		#获取当前网页URL
		currentPageUrl = self.driver.current_url
		print currentPageUrl
		self.assertEqual(currentPageUrl, "https://www.sogou.com/", "当前网页非预期!")
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()