# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_getWebElementText(self):
		url = "http://www.baidu.com"
		self.driver.get(url)
		aElement = self.driver.find_element_by_xpath("//*[@class='mnav'][1]")
		a_text = aElement.text
		print a_text

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()