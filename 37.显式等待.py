# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	from selenium import webdriver
	from selenium.webdriver.support.wait import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.common.by import By
	driver = webdriver.Firefox()
	driver.implicitly_wait(10) # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
	driver.get('https://huilansame.github.io')
	locator = (By.LINK_TEXT, 'CSDN')
	try:
		WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
		print driver.find_element_by_link_text('CSDN').get_attribute('href')
	finally:
		driver.close()

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()