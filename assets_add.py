import unittest
import time

from pageobjects.portal import login
from pageobjects import root_url
from pageobjects.portal.assets import assets


from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(root_url.portal + "/org-test-parent/login")
        login_page = login.LoginPage(self.driver, 'org-test-parent')
        login_page.navigate_to_page()
        login_page.try_to_login('tata', 'Testing*123', "Org Test Child 1")


    def test_assets(self):

        assets_page = assets.AssetsPage(self.driver, 'org-test-parent')
        assets_page.navigate_to_page()
        navbar = assets_page.navbar

        # print("table len", len(assets_page.get_assets_elements()))
        # print('Manufacturer:', assets_page.get_element_manufacturer(assets_page.get_assets_elements()[1]))
        # print('Model:', assets_page.get_element_model(assets_page.get_assets_elements()[1]))
        # print('Type:', assets_page.get_element_type(assets_page.get_assets_elements()[1]))
        # print('School', assets_page.get_element_group(assets_page.get_assets_elements()[1]))
        # print('Member', assets_page.get_element_member(assets_page.get_assets_elements()[1]))

        # print(assets_page.get_assets_list_items())
        
    def test_assets(self):

        assets_page = assets.AssetsPage(self.driver, 'org-test-parent')
        assets_page.navigate_to_page()
        navbar = assets_page.navbar

        # print("table len", len(assets_page.get_assets_elements()))
        # print('Manufacturer:', assets_page.get_element_manufacturer(assets_page.get_assets_elements()[1]))
        # print('Model:', assets_page.get_element_model(assets_page.get_assets_elements()[1]))
        # print('Type:', assets_page.get_element_type(assets_page.get_assets_elements()[1]))
        # print('School', assets_page.get_element_group(assets_page.get_assets_elements()[1]))
        # print('Member', assets_page.get_element_member(assets_page.get_assets_elements()[1]))

        # print(assets_page.get_assets_list_items())

    def tearDown(self):
        time.sleep(7)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    exit(0)

