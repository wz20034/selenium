# -*- coding:utf-8 -*-  
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:\Program Files\Mozilla Firefox\geckodriver")

    def test_scroll(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        searchBox = self.driver.find_element_by_id("query")
        searchBox.send_keys(u"光荣之路")
        time.sleep(2)
        for i in range(3):
            searchBox.send_keys(Keys.DOWN)
            time.sleep(1)
        searchBox.send_keys(Keys.ENTER)
        time.sleep(3)
        


    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()