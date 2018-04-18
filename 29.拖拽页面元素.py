# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_visitURL(self):
		url = "http://jqueryui.com/resources/demos/draggable/scroll.html"
		self.driver.get(url)
		initialPosition = self.driver.find_element_by_id("draggable")
		targetPosition = self.driver.find_element_by_id("draggable2")
		dragElement = self.driver.find_element_by_id("draggable3")
		from selenium.webdriver import ActionChains
		action_chains = ActionChains(self.driver)
		ActionChains.drag_and_drop(initialPosition, targetPosition).perform()
		for i in xrange(5):
			action_chains.drag_and_drop_by_offset(dragElement, 10, 10).perform()
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()