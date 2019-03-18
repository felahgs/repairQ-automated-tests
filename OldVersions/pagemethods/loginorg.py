################################################################
## Methods for testing related to the organization login page ##
################################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


## Return the name of the customer ##
def login(driver, org, username, password, group_index):
    """
        Login to the repairQ page

        Args:
            org (string): Organization to login
            driver (Object): Reference to the browser driver
            user: RepairQ user's login
            password: RepairQ user's password
            group_index: Index of the group to login

       Raises:
            LoginFailed - If the login is not sucessfull
            
        Returns:
            none
    """

    ## Open the login page
    driver.get('http://localhost:3000/portal/' + org + '/login')

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)
    elem = wait.until(EC.element_to_be_clickable((By.ID, 'username')))

    # Fill the login fields
    elem = driver.find_element_by_id("username")
    elem.send_keys(username)
    elem = driver.find_element_by_id("password")
    elem.send_keys(password)

    # Try to log in 
    select = Select(driver.find_element_by_id("group"))
    select.select_by_index(group_index) 
    btn = driver.find_element_by_xpath("//button[text()='Log in']")
    btn.click()

    # Wait to check if the login is successfull
    elem = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'loader-wrapper')))
        # loading is visible
    elem = wait.until(EC.invisibility_of_element((By.CLASS_NAME, 'loader-wrapper')))
        # loading is NOT visible

    try:
        error = driver.find_element_by_class_name('login-error-wrapper')
    except NoSuchElementException:
        print('RepairQ Login Success')
        return True
    else:
        # print(" ".join([x.capitalize() for x in org.split("-")]), 'Login Error:', error.get_attribute("innerHTML") )
        print(" ".join([x.capitalize() for x in org.split("-")]), 'Login Error:', error.find_element_by_tag_name('p').get_attribute("innerHTML") )
        return False
