# -*- coding:utf-8 -*-  
from selenium import webdriver
import unittest
import traceback
import time

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:\Program Files\Mozilla Firefox\geckodriver")

    def test_scroll(self):
        url = "http://www.acfun.cn"
        try:
            self.driver.get(url)
            self.driver.execute_script("window.scrollTo(100, document.body.scrollHeight);")
            time.sleep(3)
            self.driver.execute_script("document.getElementById('choice').scrollIntoView(true);")
            time.sleep(3)
            self.driver.execute_script("window.scrollBy(0, 400);")
            time.sleep(3)
        except Exception, e:
            print traceback.print_exc()
        


    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()