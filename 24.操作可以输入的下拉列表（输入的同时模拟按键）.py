# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_openateMultipleOptionDropList(self):
		url = r"file:///C:/Users/Administrator/Desktop/seleniumTestCase/24test.html"
		self.driver.get(url)
		from selenium.webdriver.common.keys import Keys
		self.driver.find_element_by_id("select").clear()
		time.sleep(1)
		self.driver.find_element_by_id("select").send_keys("c", Keys.ARROW_DOWN)
		self.driver.find_element_by_id("select").send_keys(Keys.ARROW_DOWN)
		self.driver.find_element_by_id("select").send_keys(Keys.ENTER)
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()