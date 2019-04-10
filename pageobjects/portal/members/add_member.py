from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from pageobjects import root_url
from pageobjects.basepage import BasePage
from pageobjects.repairq.customergroups import groupdetails
from pageobjects.portal import navbar


class AddMemberPage(BasePage):
    CONTENT = (By.CLASS_NAME, 'rq-content')

    # Fields
    # URL = root_url.repairq + "/customerGroups/add"
    FIRST_NAME = (By.ID, 'input-member-first-name')
    LAST_NAME = (By.ID, 'input-member-last-name')
    PHONE = (By.ID, 'input-member-primary-phone')
    EMAIL = (By.ID, 'input-member-email')

    # Button
    SAVE_BTN = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]/div/form/div[6]/button')

   
    def __init__(self, driver, org):
        self.driver = driver
        self.org = org
        self.navbar = navbar.NavBar(self.driver)
        self.URL = root_url.portal + '/' + self.org + '/members/new'
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.presence_of_element_located(AddMemberPage.CONTENT))


    def navigate_to_page(self):
        self.driver.get(self.URL)
        self.wait.until(EC.presence_of_element_located(AddMemberPage.CONTENT))

    def set_first_name(self, model: str):
        elem = self.driver.find_element(*AddMemberPage.FIRST_NAME)
        elem.send_keys(model)

    def set_last_name(self, man: str):
        elem = self.driver.find_element(*AddMemberPage.LAST_NAME)
        elem.send_keys(man)

    def set_phone(self, type: str):
        elem = self.driver.find_element(*AddMemberPage.PHONE)
        elem.send_keys(type)

    def set_email(self, group: str):
        elem = self.driver.find_element(*AddMemberPage.EMAIL)
        elem.send_keys(group)

    def save_member(self):
        btn = self.driver.find_element(*AddMemberPage.SAVE_BTN)
        btn.click()
    
    def add_new_member(self, member):
        self.set_first_name(member.get('first_name'))
        self.set_last_name(member.get('last_name'))
        self.set_phone(member.get('phone'))
        self.set_email(member.get('email'))
        self.save_member()
