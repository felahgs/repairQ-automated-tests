from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pageobjects.basepage import BasePage

class LoginPage(BasePage):
    LOGIN_SCREEN = (By.CLASS_NAME, 'with-welcome-screen')
    USER_NAME = (By.ID, 'UserLoginForm_username')
    PASSWORD = (By.ID, 'UserLoginForm_password')
    LOCATION_SEL = (By.XPATH, '//*[@id="UserLoginForm_currentLocation"]')
    LOGIN_BTN = (By.XPATH,'//*[@id="yw0"]/fieldset/div[4]/div[2]/button')
    LOGIN_ERROR = (By.CLASS_NAME, "login-error-wrapper")
    URL = 'https://cinq.repairq.io/site/login'

    def __init__(self, driver):
        self.driver = driver
        # self.URL = 'https://cinq.repairq.io/site/login'
        self.wait = WebDriverWait(driver, 10)
        LoginPage.navigate_to_page(self)
        self.wait.until(EC.presence_of_element_located(LoginPage.LOGIN_SCREEN))

    def navigate_to_page(self):
        self.driver.get(LoginPage.URL)
        self.wait.until(EC.presence_of_element_located(LoginPage.LOGIN_SCREEN))

    def set_username(self, username: str):
        elem = self.driver.find_element(*LoginPage.USER_NAME)
        elem.send_keys(username)

    def set_password(self, password: str):
        elem = self.driver.find_element(*LoginPage.PASSWORD)
        elem.send_keys(password)

    def select_location_by_index(self, location_index: int):
        select = Select(self.driver.find_element(*LoginPage.LOCATION_SEL))
        select.select_by_index(location_index)


    def try_to_login (self, username: str, password: str, location_index: int = 1):
        """
            Login to the repairQ page

            Args:
                user: RepairQ user's login
                password: RepairQ user's password
                group_index: Index of the group to login
                
            Returns:
                True if login is successfull and False otherwise
        """
        LoginPage.set_username(self, username)
        LoginPage.set_password(self, password)
        LoginPage.select_location_by_index(self, location_index)
        btn = self.driver.find_element(*LoginPage.LOGIN_BTN)
        btn.click()

        try:
            self.wait.until(EC.url_to_be('https://cinq.repairq.io/'))
        except TimeoutException:
            error = self.driver.find_element_by_class_name('help-inline')
            # print('RepairQ Login Error:', error.get_attribute("innerHTML") )
            return False
        else:
            # print('RepairQ Login Success')
            return True