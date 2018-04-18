# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_simulationLeftClickMouseOfProcess(self):
		url = r"file:///C:\Users\Administrator\Desktop\seleniumTestCase\33test.html"
		self.driver.get(url)
		div = self.driver.find_element_by_id("div1")
		from selenium.webdriver import ActionChains
		ActionChains(self.driver).click_and_hold(div).perform()
		time.sleep(3)
		ActionChains(self.driver).release(div).perform()
		time.sleep(3)
		ActionChains(self.driver).click_and_hold(div).perform()
		time.sleep(3)
		ActionChains(self.driver).release(div).perform()
		time.sleep(3)
			
	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()