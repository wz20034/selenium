# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time


class OpenTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:\Program Files\Mozilla Firefox\geckodriver")

    def test_visitURL(self):
        visitURL = "http://www.baidu.com"
        self.driver.get(visitURL)
        #通过driver对象的get方法，访问指定的网址
        assert self.driver.title.find(u"百度一下") >= 0, "assert error"
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
