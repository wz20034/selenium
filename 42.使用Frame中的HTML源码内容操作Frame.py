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

    def test_HandleFrameByPageSource(self):
    	from selenium.webdriver.support import expected_conditions as EC
    	from selenium.webdriver.support.ui import WebDriverWait
    	from selenium.common.exceptions import TimeoutException

    	url = r"file:///C:/Users/Administrator/Desktop/seleniumTestCase/frameset.html"
    	self.driver.get(url)
    	framesList = self.driver.find_elements_by_tag_name("frame")
    	for frame in framesList:
    		self.driver.switch_to.frame(frame)
    		if u"中间frame" in self.driver.page_source:
    			p = self.driver.find_element_by_xpath("//p")
    			self.assertAlmostEqual(u"这是中间frame页面上的文字", p.text)
    			self.driver.switch_to.default_content()
    			break
    		else:
    			self.driver.switch_to.default_content()
    	time.sleep(3)
    			
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()