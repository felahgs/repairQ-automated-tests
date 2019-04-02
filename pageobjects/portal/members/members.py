from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from pageobjects import root_url
from pageobjects.basepage import BasePage
from pageobjects.repairq.customergroups import groupdetails


class CustomerGroupsPage(BasePage):
    CUSTOMER_GROUP_PAGE = (By.CLASS_NAME, 'c-customerGroups')
    CUSTOMER_GROUP = (By.CLASS_NAME, 'largest-row') 
    PAGE_NAVIGATION = (By.ID, 'yw2')
    NEXT_BTN = (By.CLASS_NAME, 'next')
    CGROUP_DETAILS_BTN = (By.CLASS_NAME, 'icon-zoom-in')

def __init__(self, driver):
    self.driver = driver
    self.URL = root_url.repairq + '/customerGroups'
    self.wait = WebDriverWait(driver, 10)
    self.wait.until(EC.presence_of_element_located(CustomerGroupsPage.CUSTOMER_GROUP_PAGE))

