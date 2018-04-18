# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time
import sys

reload(sys)
sys.setdefaultencoding("utf-8")  
class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def isElementPresent(self, by, value):
		from selenium.common.exceptions import NoSuchElementException
		try:
			element = self.driver.find_element(by = by, value = value)
		except NoSuchElementException, e:
			print e
			return False
		else:
			return True

	def test_isElementPresent(self):
		url = "http://www.sogou.com"
		self.driver.get(url)
		res = self.isElementPresent("id", "query")
		if res is True:
			print u"成功"
		else:
			print u"失败"
		time.sleep(3)

	 def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()