from selenium.webdriver.common.by import By


class LoginPage:
    def __int__(self, driver):
        self.driver = driver

        self.textbox_username_id = "Email"
        self.textbox_password_id = "Password"
        self.button_login_xpath = "//button[normalize-space()='Log in']"
        self.link_logout_linkText = "Logout"

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linkText).click()
