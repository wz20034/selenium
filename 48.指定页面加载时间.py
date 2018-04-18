# -*- coding:utf-8 -*-  
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import sys

reload(sys)

sys.setdefaultencoding('utf-8')

class OpenTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:\Program Files\Mozilla Firefox\geckodriver")

    def test_PageLoadTime(self):
        self.driver.set_page_load_timeout(4)
        self.driver.maximize_window()
        try:
            startTime = time.time()
            url = "http://mail.126.com/"
            self.driver.get(url)
        except TimeoutException:
            print u'页面加载超过设定时间，超时'
            self.driver.execute_script('window.stop()')
        end = time.time() - startTime
        print end
        self.driver.switch_to.frame("x-URS-iframe")
        userName = self.driver.find_element_by_xpath("//input[@name='email']")
    	userName.send_keys("wz20034")  
        pwd =  self.driver.find_element_by_xpath("//input[@name='password']")
        pwd.send_keys("a1b2c3d4e5")
        pwd.send_keys(Keys.RETURN)
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()