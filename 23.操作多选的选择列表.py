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

	def test_operateMultipleOptionDropList(self):
		url = "file:///C:/Users/Administrator/Desktop/seleniumTestCase/23test.html"
		self.driver.get(url)
		from selenium.webdriver.support.ui import Select
		select_element = Select(self.driver.find_element_by_xpath("//select"))
		select_element.select_by_visible_text("shanzha")
		select_element.select_by_value("mihoutao")
		for option in select_element.select.all_selected_options:
			print option.text
		select_element.deselect_all()
		time.sleep(2)
		print "----3----"
		select_element.select_by_index()
		select_element.select_by_visible_text("lizhi")
		select_element.select_by_value("juzi")

		select_element.deselect_by_visible_text("lizhi")
		select_element.deselect_by_index(1)
		select_element.deselect_by_value("juzi")
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()