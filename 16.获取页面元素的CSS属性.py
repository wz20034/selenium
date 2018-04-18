# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_getWebElementCssValue(self):
		url = "http://www.baidu.com"
		self.driver.get(url)
		searchBox = self.driver.find_element_by_id("kw")
		print u"搜索输入框的高度是：", searchBox.value_of_css_property("height")
		print u"搜索输入框的宽度是：", searchBox.value_of_css_property("width")
		font = searchBox.value_of_css_property("font-family")
		print u"搜索输入框的字体是：", font
		self.assertEqual(font, "arial")
		
	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()