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


class AssetsPage(BasePage):
    CONTENT = (By.CLASS_NAME, 'rq-content')
    TABLE = (By.CLASS_NAME, 'rq-table')
    NAV_BAR = (By.CLASS_NAME, 'rq-navbar-nav')

    def __init__(self, driver, org):
        self.driver = driver
        self.org = org
        self.navbar = navbar.NavBar(self.driver)
        self.URL = root_url.portal + '/' + self.org + '/assets'
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.presence_of_element_located(AssetsPage.CONTENT))

    def navigate_to_page(self):
        self.driver.get(self.URL)
        self.wait.until(EC.presence_of_element_located(AssetsPage.CONTENT))

    def get_assets_elements(self):
        table = self.driver.find_element(*AssetsPage.TABLE)
        elements = table.find_element(By.TAG_NAME, 'tbody')
        return elements.find_elements(By.TAG_NAME, "tr")

    def get_assets_list_items(self):
        return [{
                'manufacturer': self.get_element_manufacturer(el), 
                'model':self.get_element_model(el),
                'type':self.get_element_type(el),
                'group':self.get_element_group(el),
                'member':self.get_element_member(el)
            } for el in self.get_assets_elements()]
        

    def get_element_manufacturer(self, element):
        field = element.find_elements(By.TAG_NAME, 'td')[1]
        return field.find_element_by_tag_name("a").get_attribute("innerHTML").strip()

    def get_element_model(self, element):
        field = element.find_elements(By.TAG_NAME, 'td')[2]
        return field.find_element_by_tag_name("a").get_attribute("innerHTML").strip()

    def get_element_type(self, element):
        field = element.find_elements(By.TAG_NAME, 'td')[3]
        return field.find_element_by_tag_name("a").get_attribute("innerHTML").strip()

    def get_element_group(self, element):
        field = element.find_elements(By.TAG_NAME, 'td')[4]
        return field.find_element_by_tag_name("a").get_attribute("innerHTML").strip()

    def get_element_member(self, element):
        field = element.find_elements(By.TAG_NAME, 'td')[5]
        return field.find_element_by_tag_name("a").get_attribute("innerHTML").strip()

    def get_asset_element_by_id(self, index):
        return self.get_assets_elements()[index]

    
