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


class AddAssetPage(BasePage):
    CONTENT = (By.CLASS_NAME, 'rq-content')

    # Fields
    URL = root_url.repairq + "/customerGroups/add"
    MODEL = (By.XPATH, '//*[@id="input-asset-model"]')
    MANUFACTURER = (By.XPATH, '//*[@id="input-asset-manufacturer"]')
    TYPE = (By.XPATH, '//*[@id="input-asset-type"]')
    GROUP = (By.XPATH, '//*[@id="input-asset-group"]')

    # Button
    SAVE_BTN = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]/div/form/div[5]/button')

   
    def __init__(self, driver, org):
        self.driver = driver
        self.org = org
        self.navbar = navbar.NavBar(self.driver)
        self.URL = root_url.portal + '/' + self.org + '/assets/new'
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.presence_of_element_located(AddAssetPage.CONTENT))


    def navigate_to_page(self):
        self.driver.get(AddAssetPage.URL)
        self.wait.until(EC.presence_of_element_located(AddAssetPage.CONTENT))

    def set_model(self, model: str):
        elem = self.driver.find_element(*AddAssetPage.MODEL)
        elem.send_keys(model)

    def set_manufacturer(self, man: str):
        elem = self.driver.find_element(*AddAssetPage.MANUFACTURER)
        elem.send_keys(man)

    def set_type(self, type: str):
        elem = self.driver.find_element(*AddAssetPage.TYPE)
        elem.send_keys(type)

    def set_group(self, group: str):
        elem = self.driver.find_element(*AddAssetPage.GROUP)
        elem.send_keys(group)

    def save_asset(self):
        btn = self.driver.find_element(*AddAssetPage.SAVE_BTN)
        btn.click()
    
    def add_new_asset(self, asset):
        self.set_model(asset.get('model'))
        # self.set_manufacturer(asset.get('maufacturer'))
        # self.set_type(asset.get('type'))
        # self.set_group(asset.get('group'))
        self.save_asset()
