# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import win32clipboard as w
import win32con

def setText(aString):
	w.OpenClipboard()
	w.EmptyClipboard()
	w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
	w.CloseClipboard()

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_rigthClickMouse(self):
		url = "http://www.baidu.com"
		self.driver.get(url)
		searchBox = self.driver.find_element_by_id("query")
		searchBox.click()
		time.sleep(3)
		ActionChains(self.driver).context_click(searchBox).perform()
		setText(u'gloryroad')
		ActionChains(self.driver).send_keys('P').perform()
		self.driver.find_element_by_id('stb').click()
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()  