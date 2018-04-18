# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time

class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_window_position(self):
		url = "http://www.baidu.com"
		self.driver.get(url)
		#获取当前浏览器在屏幕上的位置，返回字典对象
		position = self.driver.get_window_position()
		print "当前位置横坐标:" , position['x']
		print "当前位置纵坐标:" , position['y']
		#设置浏览器的位置
		self.driver.set_window_position(y=200, x=400)
		print self.driver.get_window_position()
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()