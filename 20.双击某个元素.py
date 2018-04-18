# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def  test_doubleClick(self):
		url = "file:///C:/Users/Administrator/Desktop/seleniumTestCase/20test.html"
		#url = "c://20test.html"
		self.driver.get(url)
		inputBox = self.driver.find_element_by_id("inputBox")
		from selenium.webdriver import ActionChains
		action_chains = ActionChains(self.driver)
		action_chains.double_click(inputBox).perform()
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()
