from selenium.webdriver.common.by import By

from PageObjects.Confirm import Confirm


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitles = (By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.XPATH, "div/button")
    cardText = (By.XPATH, "div/h4/a")
    checkOutItems = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitles)

    def getCardFooter(self):
        return self.driver.find_element(*CheckOutPage.cardFooter)

    def getCardText(self):
        return self.driver.find_element(*CheckOutPage.cardText)

    def getCheckOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOutItems).click()
        confirmOrder = Confirm(self.driver)
        return confirmOrder


