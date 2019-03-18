###########################################################
## Methods for testing related to the repairQ login page ##
###########################################################
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


## Return the name of the customer ##
def login(driver, user, password):
    """
        Login to the repairQ page

        Args:
            driver: Reference to the browser driver
            user: RepairQ user's login
            password: RepairQ user's password
            
        Returns:
            True if the login is successful returns false otherwise
    """
    driver.get("https://cinq.repairq.io/")

    elem = driver.find_element_by_id("UserLoginForm_username")
    elem.send_keys(user)
    elem = driver.find_element_by_id("UserLoginForm_password")
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)

    wait = WebDriverWait(driver, 10)

    try:
        elem = wait.until(EC.url_to_be('https://cinq.repairq.io/'))
    except TimeoutException:
        error = driver.find_element_by_class_name('help-inline')
        print('RepairQ Login Error:', error.get_attribute("innerHTML") )
        return False
    else:
        print('RepairQ Login Success')
        return True
