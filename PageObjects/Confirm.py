from selenium.webdriver.common.by import By


class Confirm:
    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    Text = (By.LINK_TEXT, "India")
    checkBox = (By.CSS_SELECTOR, ".checkbox-primary")
    confirm = (By.XPATH, "//input[@class='btn btn-success btn-lg']")

    def getCountryDetails(self):
        return self.driver.find_element(*Confirm.country)

    def getText(self):
        return self.driver.find_element(*Confirm.Text)

    def clickCheckBox(self):
        return self.driver.find_element(*Confirm.checkBox)

    def confirmButton(self):
        return self.driver.find_element(*Confirm.confirm)
