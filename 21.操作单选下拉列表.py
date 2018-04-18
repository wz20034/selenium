# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_printSelectText(self):
		url = "file:///C:/Users/Administrator/Desktop/seleniumTestCase/21test.html"
		self.driver.get(url)
		select = self.driver.find_element_by_name("fruit")
		all_options = select.find_elements_by_tag_name("option")
		for option in all_options:
			print option.text
			print option.get_attribute("value")
			option.click()
			time.sleep(2)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()