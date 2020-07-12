import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe")
        #driver = None
        #self.assertIsNone(driver)
        self.assertIsNotNone(driver)

if __name__ == "__main__":
    unittest.main()