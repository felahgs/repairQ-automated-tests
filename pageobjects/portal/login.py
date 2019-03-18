from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from pageobjects.basepage import BasePage

class LoginPage(BasePage):
    USER_NAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    GROUP = (By.ID, 'group')
    LOGIN_BTN = (By.XPATH,"//button[text()='Log in']")
    LOGIN_ERROR = (By.CLASS_NAME, "login-error-wrapper")

    def __init__(self, driver, org):
        self.driver = driver
        self.org = org
        self.URL = 'http://localhost:3000/portal/' + self.org + '/login'
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.element_to_be_clickable(LoginPage.USER_NAME))


    def navigate_to_page(self):
        self.driver.get(self.URL)
        self.wait.until(EC.element_to_be_clickable(LoginPage.USER_NAME))

    def send_username(self, username: str):
        elem = self.driver.find_element(*LoginPage.USER_NAME)
        elem.send_keys(username)

    def send_password(self, password: str):
        elem = self.driver.find_element(*LoginPage.PASSWORD)
        elem.send_keys(password)

    def select_group(self, group_index: int):
        select = Select(self.driver.find_element(*LoginPage.GROUP))
        select.select_by_index(group_index)


    def try_to_login (self, username: str, password: str, group_index: int):
        """
            Login to the repairQ page

            Args:
                user: RepairQ user's login
                password: RepairQ user's password
                group_index: Index of the group to login
                
            Returns:
                True if login is successfull and False otherwise
        """
        LoginPage.send_username(self, username)
        LoginPage.send_password(self, password)
        LoginPage.select_group(self, group_index)
        btn = self.driver.find_element(*LoginPage.LOGIN_BTN)
        btn.click()

        # Wait to check if the login is successfull
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'loader-wrapper')))
        # loading is visible
        self.wait.until(EC.invisibility_of_element((By.CLASS_NAME, 'loader-wrapper')))
        # loading is NOT visible

        try:
            error = self.driver.find_element(*LoginPage.LOGIN_ERROR)
        except NoSuchElementException:
            # print('RepairQ Login Success')
            return True
        else:
            # print(" ".join([x.capitalize() for x in self.org.split("-")]), 'Login Error:', error.find_element_by_tag_name('p').get_attribute("innerHTML") )
            return False