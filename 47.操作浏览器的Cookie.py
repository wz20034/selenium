# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
import time
import sys

reload(sys)

sys.setdefaultencoding('utf-8')

class OpenTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:\Program Files\Mozilla Firefox\geckodriver")

    def test_Cookie(self):
    	url = "http://www.sogou.com"
    	self.driver.get(url)
    	cookies = self.driver.get_cookies()
        for cookie in cookies:
            print "%s -> %s -> %s -> %s -> %s" %(cookie['domain'], cookie["name"], cookie["value"], cookie["expiry"], cookie["path"])
        # ck = self.driver.get_cookies("SUV")
        # print "%s -> %s -> %s -> %s -> %s" %(ck['domain'], ck["name"], ck["value"], ck["expiry"], ck["path"])
        print self.driver.delete_cookie("ABTEST")
        self.driver.add_cookie({"name":"gloryroadTrain", 'value':'1479697159269020'})
        cookie = self.driver.get_cookie("gloryroadTrain")
        print cookie
    	time.sleep(3)
    			
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()