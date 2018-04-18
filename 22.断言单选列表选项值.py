# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	#22 断言单选列表选项值
	def test_checkSelectText(self):
		url = r"file:///C:/Users/Administrator/Desktop/seleniumTestCase/22test.html"
		self.driver.get(url)
		from selenium.webdriver.support.ui import Select
		select_element = Select(self.driver.find_element_by_xpath("//select"))
		actual_options = select_element.options
		expect_optionsList = ['taozi', 'xigua', 'juzi', 'mihoutao', 'shanzha', 'lizhi']
		actual_optionsList = map(lambda option: option.text, actual_options)
		self.assertEqual(expect_optionsList, actual_optionsList)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()
