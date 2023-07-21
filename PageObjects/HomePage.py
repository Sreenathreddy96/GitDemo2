from selenium.webdriver.common.by import By

from PageObjects.CheckOutPage import CheckOutPage
from selenium.webdriver.support.select import Select

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    Shop = (By.CSS_SELECTOR, "[href*='shop']")
    Name = (By.NAME, "name")
    Email = (By.NAME, "email")
    Password = (By.ID, "exampleInputPassword1")
    Check = (By.ID, "exampleCheck1")
    Submit = (By.CSS_SELECTOR, ".btn-success")
    Gender = (By.ID, "exampleFormControlSelect1")
    Message = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.Shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.Name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.Email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.Password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.Check)

    def submitForm(self):
        return self.driver.find_element(*HomePage.Submit)

    def selectOptionByText(self):
        self.driver.find_element(*HomePage.Gender)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.Message)