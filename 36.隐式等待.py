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

	from selenium.common.exceptions import NoSuchElementException, TimeoutException
	import traceback
	def test_implictWait(self):
		url = "http://www.sogou.com"
		self.driver.get(url)
		self.driver.implictly_wait(10)

		try:
			searchBox = self.driver.find_element_by_id("query")
			searchBox.send_keys(u"光荣之路自动化测试")
			click = self.driver.find_element_by_id("stb")
			click.click()
		except Exception, e:
			traceback.print_exc()

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()