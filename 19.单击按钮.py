# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_visitURL(self):
		url = "file:///C:\Users\Administrator\Desktop\seleniumTestCase\19test.html"
		self.driver.get(url)
		button = self.driver.find_element_by_id("button")
		button.click()
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()