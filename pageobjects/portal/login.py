from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pageobjects import root_url

from pageobjects.basepage import BasePage

class LoginPage(BasePage):
    USER_NAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    GROUP = (By.ID, 'group')
    LOGIN_BTN = (By.XPATH,"//button[text()='Log in']")
    LOGIN_ERROR = (By.CLASS_NAME, "login-error-wrapper")
    LOADING_SPINNER = (By.CLASS_NAME, "rq-loading-spinner")

    def __init__(self, driver, org):
        self.driver = driver
        self.org = org
        self.URL = root_url.portal + '/' + self.org + '/login'
        self.wait = WebDriverWait(driver, 10)
        # self.wait.until(EC.element_to_be_clickable(LoginPage.USER_NAME))

    def navigate_to_page(self):
        self.driver.get(self.URL)
        self.wait.until(EC.element_to_be_clickable(LoginPage.USER_NAME))

    def set_username(self, username: str):
        elem = self.driver.find_element(*LoginPage.USER_NAME)
        elem.send_keys(username)

    def set_password(self, password: str):
        elem = self.driver.find_element(*LoginPage.PASSWORD)
        elem.send_keys(password)

    def select_group_by_index(self, group_index: int):
        select = Select(self.driver.find_element(*LoginPage.GROUP))
        select.select_by_index(group_index)

    def select_group_by_name(self, group_name: str):
        select = Select(self.driver.find_element(*LoginPage.GROUP))
        select.select_by_visible_text(group_name)

    def group_list_itens(self):
        select = self.driver.find_element(*LoginPage.GROUP)
        opts = select.find_elements(By.TAG_NAME, 'option')
        return [opt.get_attribute('innerHTML') for opt in opts if opt.get_attribute('value') is not '' ]

    def try_to_login (self, username: str, password: str, group_name: str):
        """
            Login to the repairQ page

            Args:
                user: RepairQ user's login
                password: RepairQ user's password
                group_name: Name of the group to login
                
            Returns:
                True if login is successfull and False otherwise
        """
        LoginPage.set_username(self, username)
        LoginPage.set_password(self, password)
        LoginPage.select_group_by_name(self, group_name)
        btn = self.driver.find_element(*LoginPage.LOGIN_BTN)
        btn.click()

        # Wait to check if the login is successfull
        self.wait.until(EC.presence_of_element_located((LoginPage.LOADING_SPINNER)))
        # loading is visible
        self.wait.until(EC.invisibility_of_element((LoginPage.LOADING_SPINNER)))
        # loading is NOT visible

        try:
            error = self.driver.find_element(*LoginPage.LOGIN_ERROR)
        except NoSuchElementException:
            # print('RepairQ Login Success')
            return True
        else:
            # print(" ".join([x.capitalize() for x in self.org.split("-")]), 'Login Error:', error.find_element_by_tag_name('p').get_attribute("innerHTML") )
            return False