from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from PageObjects.CheckOutPage import CheckOutPage
from PageObjects.Confirm import Confirm
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self,):
        log = self.logging()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all card titles")
        products = checkOutPage.getCardTitles()

        for product in products:
            # productName = product.checkOutPage.getCardText().text
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                # checkOutPage.getCardFooter().click()
                product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "[class*='btn-primary']").click()
        confirmOrder = checkOutPage.getCheckOutItems()
        log.info("Entering country as ind")
        confirmOrder.getCountryDetails().send_keys("IND")
        self.verifyLinkPresence("India")
        confirmOrder.getText().click()
        confirmOrder.clickCheckBox().click()
        confirmOrder.confirmButton().click()
        alerts = self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text
        log.info("text received from the application" + alerts)
        assert "Success! Thank you!" in alerts
