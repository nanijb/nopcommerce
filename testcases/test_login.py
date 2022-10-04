import time
import pytest

from pageobjects.LoginPage import LoginPage
from pageobjects.HomePage import HomePage
from utilities.utils import Utils


class Test_001_Login:
    baseURL = Utils.getApplicationURL()
    username = Utils.getUsername()
    password = Utils.getPassword()
    log = Utils.custom_logger()

    @pytest.mark.regression
    def test_loginPageTitle(self, setup):
        self.log.info("************* Test_001_Login *************")
        self.log.info("************* Verifying Login Page Title *************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        time.sleep(3)
        if act_title == "Your store. Login":
            assert True
            self.log.info("************* Login Page Title Test is Passed *************")
            self.driver.close()
        else:
            self.driver.save_screenshot("screenshots/test_loginPageTitle.png")
            self.driver.close()
            self.log.error("************* Login Page Title Test is Failed *************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.log.info("************* verify login test *************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage()
        self.lp.__int__(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.log.info("************* Login Test is Passed *************")
            self.hp = HomePage()
            self.hp.__int__(self.driver)
            self.hp.clickLogout()
            self.log.info("************* Logout Test is Passed *************")
            self.driver.close()
        else:
            self.driver.save_screenshot("screenshots/test_login.png")
            self.driver.close()
            self.log.error("************* Login Test is Failed *************")
            assert False
