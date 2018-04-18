# -*- coding:utf-8 -*-  
from selenium import webdriver
import unittest


class TestDemo(unittest.TestCase):

    def test_killWindowsProcess(self):
        firefoxDriver = webdriver.Firefox(executable_path="C:\Program Files\Mozilla Firefox\geckodriver")
        import os
        returnCode = os.system("taskkill /F /iM firefox.exe")
        if returnCode == 0:
            print u"成功结束Firefox浏览器进程！"
        else:
            print u"结束Firefox浏览器进程失败！"
      
if __name__ == '__main__':
    unittest.main()