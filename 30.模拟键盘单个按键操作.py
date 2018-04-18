# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def url(self):
		url = "http://www.baidu.com"
		self.driver.get(url)
		from selenium.webdriver.common.keys import Keys
		query = self.driver.find_elemnet_by_id("query")
		query.send_keys(Keys.F12)
		time.sleep(3)
		query.send_keys(Keys.F12)
		query.send_keys("selenium")
		query.send_keys(Keys.ENTER)
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()