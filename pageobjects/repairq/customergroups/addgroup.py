from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

from pageobjects.basepage import BasePage
from pageobjects.repairq.customergroups import groupdetails


class AddGroup(BasePage):
    URL = "https://cinq.repairq.io/customerGroups/add"
    MENU = (By.CLASS_NAME, "left-menu-content")
    NAME_IN = (By.ID, 'CustomerGroup_name')
    DESCRIPTION_IN = (By.ID, 'CustomerGroup_description')
    ACTIVE_SEL = (By.ID, 'CustomerGroup_is_active')
    LOCATION_SEL = (By.ID, 'CustomerGroup_location_id')
    PARENT_SEL = (By.ID, 'CustomerGroup_parent_id')
    SAVE_BTN = (By.ID, 'save-button')


   
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.presence_of_element_located(AddGroup.MENU))


    def navigate_to_page(self):
        self.driver.get(AddGroup.URL)
        self.wait.until(EC.presence_of_element_located(AddGroup.MENU))

    def set_name(self, name: str):
        elem = self.driver.find_element(*AddGroup.NAME_IN)
        elem.send_keys(name)

    def set_description(self, desc: str):
        elem = self.driver.find_element(*AddGroup.DESCRIPTION_IN)
        elem.send_keys(desc)

    def select_active(self, state: bool):
        select = Select(self.driver.find_element(*AddGroup.ACTIVE_SEL))
        index = 0 if state is True else 1
        select.select_by_index(index)

    def select_location_by_index(self, index: int):
        select = Select(self.driver.find_element(*AddGroup.LOCATION_SEL))
        select.select_by_index(index)

    def select_location_by_text(self, location: str):
        select = Select(self.driver.find_element(*AddGroup.LOCATION_SEL))
        select.select_by_visible_text(location)

    def select_parent_by_index(self, index: int):
        select = Select(self.driver.find_element(*AddGroup.PARENT_SEL))
        select.select_by_index(index)

    def select_parent_by_text(self, parent: str):
        select = Select(self.driver.find_element(*AddGroup.PARENT_SEL))
        select.select_by_visible_text(parent)

    def save_group(self):
        btn = self.driver.find_element(*AddGroup.SAVE_BTN)
        btn.click()