from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

from pageobjects.basepage import BasePage
from pageobjects.repairq.customergroups import groupdetails


class AddUser(BasePage):
    URL = "https://cinq.repairq.io/customerGroupUsers/add"
    FIRST_NAME = (By.ID, "CustomerGroupUserForm_first_name")
    LAST_NAME = (By.ID, "CustomerGroupUserForm_last_name")
    EMAIL = (By.ID, "CustomerGroupUserForm_email")
    PHONE = (By.ID, "CustomerGroupUserForm_pri_phone")
    USERNAME = (By.ID, "CustomerGroupUserForm_username")
    PASSWORD = (By.ID, "CustomerGroupUserForm_pin")
    PASSWORD_CONFIRM = (By.ID, "CustomerGroupUserForm_confirm_pin")
    CUSTOMER_GROUP_SELECT = (By.ID, "addCustomerGroup")
    SAVE_BTN = (By.ID, "btnAddGruop")
    ROLES_TABLE = (By.ID, "roles-table-body")
    ADD_GROUP_BTN = (By.ID, "btnAddGroup")
    CUSTOMER_GROUP = (By.TAG_NAME, "tr")
    SAVE_BTN = (By.XPATH, '//*[@id="customerGroupUser-form"]/fieldset/div[8]/button')

    def __init__(self, driver):
        self.driver = driver
        # self.URL = 'https://cinq.repairq.io/customerGroupUsers/add'
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.presence_of_element_located(AddUser.ROLES_TABLE))


    def navigate_to_page(self):
        self.driver.get(AddUser.URL)
        self.wait.until(EC.presence_of_element_located(AddUser.ROLES_TABLE))

    def set_first_name(self, first_name: str):
        elem = self.driver.find_element(*AddUser.FIRST_NAME)
        elem.send_keys(first_name)

    def set_last_name(self, last_name: str):
        elem = self.driver.find_element(*AddUser.LAST_NAME)
        elem.send_keys(last_name)

    def set_email(self, email: str):
        elem = self.driver.find_element(*AddUser.EMAIL)
        elem.send_keys(email)

    def set_phone(self, phone: str):
        elem = self.driver.find_element(*AddUser.PHONE)
        elem.send_keys(phone)

    def set_username(self, username: str):
        elem = self.driver.find_element(*AddUser.USERNAME)
        elem.send_keys(username)

    def set_password(self, password: str):
        elem = self.driver.find_element(*AddUser.PASSWORD)
        elem.send_keys(password)

    def set_password_confirmation(self, password: str):
        elem = self.driver.find_element(*AddUser.PASSWORD_CONFIRM)
        elem.send_keys(password)

    def select_customer_group(self, index: int):
        select = Select(self.driver.find_element(*AddUser.CUSTOMER_GROUP_SELECT))
        select.select_by_index(index)
        btn = self.driver.find_element(*AddUser.ADD_GROUP_BTN)
        btn.click()


    def set_role_organization_admin(self, group_index: int):
        group_index += 1
        table = self.driver.find_element(*AddUser.ROLES_TABLE)
        groups = table.find_elements_by_tag_name("tr")
        self.driver.implicitly_wait(5)
        checkbox = groups[group_index].find_elements_by_tag_name("input")[0]
        checkbox.click()


    def set_role_setting_manager(self, group_index: int):
        group_index += 1
        table = self.driver.find_element(*AddUser.ROLES_TABLE)
        groups = table.find_elements_by_tag_name("tr")
        self.driver.implicitly_wait(5)
        checkbox = groups[group_index].find_elements_by_tag_name("input")[1]
        checkbox.click()


    def set_role_staff_manager(self, group_index: int):
        group_index += 1
        table = self.driver.find_element(*AddUser.ROLES_TABLE)
        groups = table.find_elements_by_tag_name("tr")
        self.driver.implicitly_wait(5)
        checkbox = groups[group_index].find_elements_by_tag_name("input")[2]
        checkbox.click()


    def set_role_asset_manager(self, group_index: int):
        group_index += 1
        table = self.driver.find_element(*AddUser.ROLES_TABLE)
        groups = table.find_elements_by_tag_name("tr")
        self.driver.implicitly_wait(5)
        checkbox = groups[group_index].find_elements_by_tag_name("input")[3]
        checkbox.click()


    def set_role_member_manager(self, group_index: int):
        group_index += 1
        table = self.driver.find_element(*AddUser.ROLES_TABLE)
        groups = table.find_elements_by_tag_name("tr")
        self.driver.implicitly_wait(5)
        checkbox = groups[group_index].find_elements_by_tag_name("input")[4]
        checkbox.click()


    def set_role_service_manager(self, group_index: int):
        group_index += 1
        table = self.driver.find_element(*AddUser.ROLES_TABLE)
        groups = table.find_elements_by_tag_name("tr")
        self.driver.implicitly_wait(5)
        checkbox = groups[group_index].find_elements_by_tag_name("input")[5]
        checkbox.click()


    def save_contact(self):
        btn = self.driver.find_element(*AddUser.SAVE_BTN)
        btn.click()




