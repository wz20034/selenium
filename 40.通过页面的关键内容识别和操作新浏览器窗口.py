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

	def test_identifyPopUpWindoByPageSource(self):
		from selenium.common.exceptions import NoSuchWindowException, TimeoutException
		from selenium.webdriver.support import expected_conditions as EC
		from selenium.webdriver.common.by import By
		from selenium.webdriver.support.ui import WebDriverWait
		import traceback
		url = r"file:///C:/Users/Administrator/Desktop/seleniumTestCase/39test.html"
		self.driver.get(url)
		WebDriverWait(self.driver, 10, 0.2).until(EC.element_to_be_clickable((By.LINK_TEXT, 'sogou搜索'))).click()
		all_handles = self.driver.window_handles
		print self.driver.current_window_handle
		print len(all_handles)
		time.sleep(2)
		if len(all_handles) > 0:
			try:
				for windowHandle in all_handles:
					self.driver.switch_to.window(windowHandle)
					pageSource = self.driver.page_source
					if u"搜狗搜索" in pageSource:
						WebDriverWait(self.driver, 10, 0.2).until(lambda x: x.find_element_by_id("query")).send_keys(u"sogou首页的浏览器窗口被找到")
						time.sleep(2)
			except NoSuchWindowException, e:
				print traceback.print_exc()
			except TimeoutException, e:
				print traceback.print_exc()
		self.driver.switch_to.window(all_handles[0])
		self.assertTrue(u"你爱吃的水果么？" in self.driver.page_source)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()