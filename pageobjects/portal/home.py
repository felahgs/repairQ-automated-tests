from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageobjects import root_url
from pageobjects.basepage import BasePage
from pageobjects.portal import navbar

class HomePage(BasePage):
    HOME_PAGE = (By.CLASS_NAME, 'rq-home')
    NAV_BAR = (By.CLASS_NAME, 'rq-navbar-nav')
    GROUP_DROPDOWN = (By.XPATH, '//*[@id="app"]/div/nav/div/div/div[3]/ul/li[1]/label/ul')


def __init__(self, driver, org):
    self.driver = driver
    self.org = org
    self.URL = root_url.portal + self.org
    self.wait = WebDriverWait(driver, 10)
    self.wait.until(EC.visibility_of_element_located(HomePage.HOME_PAGE))

def navigate_to_page(self):
    self.driver.get(self.URL)
    self.wait.until(EC.element_to_be_clickable(HomePage.HOME_PAGE))


