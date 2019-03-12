#############################################################
## Methods for testing related to the customer groups page ##
#############################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


## Return the name of the customer ##
def login(driver, user, password):
    """
        Login to the repairQ page

        Args:
            driver: Reference to the browser driver
            user: RepairQ user's login
            password: RepairQ user's password

        Returns:
            true if the login is sucessfull and the next page is loaded 
            and returns false otherwise
    """
    driver.get("https://cinq.repairq.io/")
    elem = driver.find_element_by_id("UserLoginForm_username")
    elem.send_keys("felipe")
    elem = driver.find_element_by_id("UserLoginForm_password")
    elem.send_keys("felipe")
    elem.send_keys(Keys.RETURN)