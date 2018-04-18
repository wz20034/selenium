class OpenTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

	def test_visitURL(self):
		url = r"file:///C:/Users/Administrator/Desktop/seleniumTestCase/26test.html"
		self.driver.get(url)
		berryCheckBox = self.driver.find_element_by_xpath("//input[@value='berry']")
		berryCheckBox.click()
		self.assertTrue(berryCheckBox.is_selected(), u"草莓复选框未被选中！")
		if berryCheckBox.is_selected():
			berryCheckBox.click()
			self.asserFalse(berryCheckBox.is_selected())
		checkBoxList = self.driver.find_element_by_xpath("//input[@name='fruit']")
		for box in checkBoxList:
			if not box.is_selected():
				box.click()
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == '__main__':
	unittest.main()