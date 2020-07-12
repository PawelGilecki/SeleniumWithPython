import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe")
        driver.get("https://www.google.com/")
        titleOfWebPage = driver.title

        #assertEqual
        #self.assertEqual("Google", titleOfWebPage, "webpage title is not the same")
        self.assertNotEqual("Google", titleOfWebPage)
if __name__ == "__main__":
    unittest.main()