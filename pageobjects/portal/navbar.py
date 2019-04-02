from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from pageobjects import root_url
from pageobjects.basepage import BasePage

class NavBar(BasePage):
    ASSETS = (By.XPATH, '//*[@id="app"]/div/nav/div/div/div[2]/ul/li[1]')
    USERS = (By.XPATH, '//*[@id="app"]/div/nav/div/div/div[2]/ul/li[2]')
    INVENTORY = (By.XPATH, '//*[@id="app"]/div/nav/div/div/div[2]/ul/li[3]')
    SETTINGS = (By.XPATH, '//*[@id="app"]/div/nav/div/div/div[2]/ul/li[4]')

    GROUP_DROPDOWN = (By.XPATH, '//*[@id="app"]/div/nav/div/div/div[3]/ul/li[1]/label/ul')
    LANG_DROPDOWN = (By.XPATH, '//*[@id="app"]/div/nav/div/div/div[3]/ul/li[2]/label/ul')
    USER_DROPDOWN = (By.XPATH, '//*[@id="app"]/div/nav/div/div/div[3]/ul/li[3]/label/ul')

    LOGOUT_BTN = (By.XPATH, '//*[@id="app"]/div/nav/div/div/div[3]/ul/li[3]/label/ul/li[2]/button')

def __init__(self, driver, org):
    self.driver = driver

def assets_click(self):
    elem = self.driver.find_element(*NavBar.ASSETS)
    elem.click()

def users_click(self):
    elem = self.driver.find_element(*NavBar.USERS)
    elem.click()
    
def inventory_click(self):
    elem = self.driver.find_element(*NavBar.INVENTORY)
    elem.click()

def settings_click(self):
    elem = self.driver.find_element(*NavBar.SETTINGS)
    elem.click()

def group_dropdown_elements(self):
    return self.driver.find_elements(NavBar.GROUP_DROPDOWN)

def lang_dropdown_elements(self):
    return self.driver.find_elements(NavBar.LANG_DROPDOWN)

def user_dropdown_elements(self):
   return self.driver.find_elements(NavBar.USER_DROPDOWN)

def change_group_by_index(self, index):
    elem = self.group_dropdown_elements[index]
    elem.click()


def select_lang_by_index(self, index):
    elem = self.lang_dropdown_elements[index]
    elem.click()

def logout(self):
    elem = self.driver.find_element(NavBar.LOGOUT_BTN)[1]
    elem.click()





