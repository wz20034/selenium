# -*- coding:utf-8 -*-  
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import unittest
import traceback
import time

class TestDemo(unittest.TestCase):
	def setUp(self):
	    self.driver = webdriver.Firefox(executable_path="C:\Program Files\Mozilla Firefox\geckodriver")

	def test_excecuteScript(self):
		url = "http://www.baidu.com"
		self.driver.get(url)
		searchInputBoxJS = "document.getElementById('kw').value='光荣之路';"
		searchButtonJS = "document.getElementById('su').click()"
		try:
			self.driver.execute_script(searchInputBoxJS)
			time.sleep(3)
			self.driver.execute_script(searchButtonJS)
			time.sleep(3)
			self.assertTrue(u"百度百科" in searchButtonJS.driver.page_source)
		except WebDriverException, e:
			print u"在页面中没有找到要操作的页面元素", traceback.print_exc()
		except AssertionError, e:
			print u"页面不存在断言的关键字串"
		except Exception, e:
			print traceback.print_exc()
		time.sleep(3)
				
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()
