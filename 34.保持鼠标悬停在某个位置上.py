# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time
import sys

reload(sys)

sys.setdefaultencoding('utf-8')


class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_roverOnElement(self):
		url = r"file:///C:/Users/Administrator/Desktop/seleniumTestCase/34test.html"
		self.driver.get(url)
		link1 = self.driver.find_element_by_link_text(u"鼠标指过来1")
		link2 = self.driver.find_element_by_link_text(u"鼠标指过来2")
		p = self.driver.find_element_by_xpath("//p")
		print link1.text, link2.text
		from selenium.webdriver import ActionChains
		ActionChains(self.driver).move_to_element(link1).perform()
		time.sleep(3)
		ActionChains(self.driver).move_to_element(p).perform()
		time.sleep(3)
		ActionChains(self.driver).move_to_element(link2).perform()
		time.sleep(3)
		ActionChains(self.driver).move_to_element(p).perform()
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()