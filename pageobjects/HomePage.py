from selenium.webdriver.common.by import By


class HomePage:
    def __int__(self, driver):
        self.driver = driver

        self.link_logout_linkText = "Logout"

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linkText).click()
