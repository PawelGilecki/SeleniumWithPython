import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe")
        driver.get("https://www.google.com/")
        titleOfWebPage = driver.title

        #self.assertTrue(titleOfWebPage == "Google") #True
        self.assertFalse(titleOfWebPage == "Google123")
if __name__ == "__main__":
    unittest.main()