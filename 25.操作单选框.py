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

	def test_visitURL(self):
		url = r"file:///C:/Users/Administrator/Desktop/seleniumTestCase/25test.html"
		self.driver.get(url)
		berryRadio = self.driver.find_element_by_xpath("//input[@value='berry']")
		berryRadio.click()
		self.assertTrue(berryRadio.is_selected(), u"草莓单选框未被选中！")
		if berryRadio.is_selected():
			watermelonRadio = self.driver.find_element_by_xpath("//input[@value='watermelon']")
			watermelonRadio.click()
			self.assertFalse(berryRadio.is_selected())
		radioList = self.driver.find_element_by_xpath("//input[@value='fruit']")
		for radio in radioList:
			if radio.get_attribute("value") == "orange":
				if not radio.is_selected():
					radio.click()
					self.assertEqual(radio.get_attribute("value"), "orange")
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()