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

    def test_HandleFrame(self):
    	from selenium.webdriver.support import expected_conditions as EC
    	from selenium.webdriver.support.ui import WebDriverWait
    	from selenium.common.exceptions import TimeoutException

    	url = r"file:///C:/Users/Administrator/Desktop/seleniumTestCase/frameset.html"
    	self.driver.get(url)
    	self.driver.switch_to.frame(0)
    	leftFrameText = self.driver.find_element_by_xpath("//p")
    	self.assertAlmostEqual(leftFrameText.text, u"这是左侧frame页面上的文字")
    	self.driver.find_element_by_tag_name("input").click()
    	try:
    		alertWindow = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
    		print alertWindow.text
    		alertWindow.accept()
    	except TimeoutException, e:
    		print e
		self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("frame")[1])
		assert u"这是中间 frame 页面上的文字" in self.driver.page_source
    	self.driver.find_element_by_tag_name("input").send_keys(u"我在中间frame")
    	self.driver.switch_to.default_content()
    	self.driver.switch_to.frame(self.driver.find_element_by_id("rightframe"))
    	assert u"这是右侧frame页面上的文字" in self.driver.page_source
    	self.driver.switch_to.default_content()
    	time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
