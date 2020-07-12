from selenium import webdriver
import pytest

class TestOrangeHRM():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homePageTitle(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert self.driver.title == "OrangeHRM"

    def test_login(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title == "OrangeHRM"