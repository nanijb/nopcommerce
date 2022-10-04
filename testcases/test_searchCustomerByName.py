import time
import pytest
from pageobjects.LoginPage import LoginPage
from pageobjects.AddcustomerPage import AddCustomer
from pageobjects.SearchCustomerPage import SearchCustomer
from utilities.utils import Utils


class Test_SearchCustomerByName_005:
    baseURL = Utils.getApplicationURL()
    username = Utils.getUsername()
    password = Utils.getPassword()
    logger = Utils.custom_logger()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage()
        self.lp.__int__(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Name **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(2)

        self.logger.info("************* searching customer by Name **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")
