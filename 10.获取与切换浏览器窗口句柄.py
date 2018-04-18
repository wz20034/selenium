# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_operateWindowHandle(self):
		url = "http://www.baidu.com"
		self.driver.get(url)
		now_handle = self.driver.current_window_handle
		print now_handle
		self.driver.find_element_by_id("kw").send_keys("w3cschool")
		self.driver.find_element_by_id("su").click()
		time.sleep(3)
		self.driver.find_element_by_xpath('//div[@id="1"]//a[text()="w3"]').click()
		time.sleep(5)
		all_handles = self.driver.window_handles
		print "++++", self.driver.window_handles[-1]
		for handle in all_handles:
			if handle != now_handle:
				self.driver.switch_to.window(handle)
		self.driver.find_element_by_link_text('HTML5').click()
		time.sleep(3)
		self.driver.close()
		time.sleep(3)
		print now_handle
		self.driver.switch_to.window(now_handle)
		time.sleep(2)
		self.driver.find_element_by_id("kw").clear()
		self.driver.find_element_by_id("kw").send_keys(u"光荣之路自动化测试培训")
		self.driver.find_element_by_id("su").click()
		time.sleep(5)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()