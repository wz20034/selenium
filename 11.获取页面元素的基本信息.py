# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_getBasicInfo(self):
		url = "http://www.baidu.com"
		self.driver.get(url)
		newsElement = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/a[1]')
		print "tag：", newsElement.tag_name
		print "size：", newsElement.size

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()