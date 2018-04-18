# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_getWebElementIsEnabled(self):
		url = r"file:///C:/Users/Administrator/Desktop/seleniumTestCase/14test.html"
		self.driver.get(url)
		input1 = self.driver.find_element_by_id("input1")
		print input1.is_enabled()
		input2 = self.driver.find_element_by_id("input2")
		print input2.is_enabled()
		input3 = self.driver.find_element_by_id("input3")
		print input3.is_enabled()

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()