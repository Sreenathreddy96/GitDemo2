import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pytest import ExitCode

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass



class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.logging()
        homepage = HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["Email"])
        homepage.getPassword().send_keys(getData["password"])
        homepage.getCheckbox().click()
        dropdown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        dropdown.select_by_visible_text(getData["gender"])
        homepage.submitForm().click()
        message = homepage.getSuccessMessage().text
        assert "success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.foo())

    def getData(self, request):
        return request.param







        #driver.find_element(By.NAME, "name").send_keys("Rahul")
        #driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
        #driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
        #driver.find_element(By.ID, "exampleCheck1").click()
        #dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        #dropdown.select_by_visible_text("Male")
        #driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

        #message = driver.find_element(By.CLASS_NAME, "alert-success").text

        #assert "success" in message



