from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from pageobjects.basepage import BasePage

class NavBar(BasePage):
    ASSETS = (By.XPATH, '//*[@id="app"]/div/nav/div/div/div[2]/ul/li[1]')
    USERS = (By.XPATH, '//*[@id="app"]/div/nav/div/div/div[2]/ul/li[2]')
    INVENTORY = (By.XPATH, '//*[@id="app"]/div/nav/div/div/div[2]/ul/li[3]')
    SETTINGS = (By.XPATH, '//*[@id="app"]/div/nav/div/div/div[2]/ul/li[4]')

    GROUP_DROPDOWN = (By.XPATH, '//*[@id="app"]/div/nav/div/div/div[3]/ul/li[1]/label')
    LANG_DROPDOWN = (By.XPATH, '//*[@id="app"]/div/nav/div/div/div[3]/ul/li[2]/label')
    USER_DROPDOWN = (By.XPATH, '//*[@id="app"]/div/nav/div/div/div[3]/ul/li[3]/label')

    DROPDOWN_ITEM = (By.CLASS_NAME, 'rq-dropdown-nav__item')
    DROPDOWN_BTN = (By.CLASS_NAME, 'rq-dropdown-nav__button')

    LOGOUT_BTN = (By.XPATH, '//*[@id="app"]/div/nav/div/div/div[3]/ul/li[3]/label/ul/li[2]/button')

    def __init__(self, driver):
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
        elem = self.driver.find_element(*NavBar.GROUP_DROPDOWN)
        return elem.find_elements(*NavBar.DROPDOWN_ITEM)

    def lang_dropdown_elements(self):
        elem = self.driver.find_element(*NavBar.LANG_DROPDOWN)
        return elem.find_elements(*NavBar.DROPDOWN_ITEM)

    def user_dropdown_elements(self):
        elem = self.driver.find_element(*NavBar.USER_DROPDOWN)
        return elem.find_elements(*NavBar.DROPDOWN_ITEM)

    def get_groups_dropdown_items(self):
        elements = self.group_dropdown_elements()
        return [elem.find_element(By.TAG_NAME, "button").get_attribute('innerHTML') for elem in elements]

    def get_langs_dropdown_items(self):
        elements = self.lang_dropdown_elements()
        return [elem.find_element(By.TAG_NAME, "button").get_attribute('innerHTML') for elem in elements]

    def get_user_dropdown_items(self):
        elements = self.user_dropdown_elements()
        return [elem.find_element(By.TAG_NAME, "button").get_attribute('innerHTML') for elem in elements]

    def change_group_by_index(self, index):
        dropdown = self.driver.find_element(*NavBar.GROUP_DROPDOWN)
        dropdown.click()
        elem = self.group_dropdown_elements()[index]
        elem.find_element(By.TAG_NAME, "button").click()

    def select_lang_by_index(self, index):
        dropdown = self.driver.find_element(*NavBar.LANG_DROPDOWN)
        dropdown.click()
        itens = dropdown.find_elements(*NavBar.DROPDOWN_ITEM)
        itens[0].click()

    def logout(self):
        elem = self.driver.find_element(NavBar.LOGOUT_BTN)[1]
        elem.click()
