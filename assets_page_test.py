import unittest
import time

from pageobjects.portal import login
from pageobjects import root_url
from pageobjects.portal.assets import add_asset
from pageobjects.portal.assets import assets


from selenium import webdriver
from selenium.webdriver.common.by import By



class Test(unittest.TestCase):
    def setUp(self):
        self.org = "school-number-10"
        self.driver = webdriver.Chrome()
        login_page = login.LoginPage(self.driver, self.org)
        login_page.navigate_to_page()
        login_page.try_to_login('fela', 'Testing*123', self.org)


    # def test_add_parent_group(self):
    #     asset_add = add_asset.AddAssetPage(self.driver, self.org)
    #     asset_add.navigate_to_page()
        
    #     customers_list = customer_groups_page.get_customers()
    #     count = len(customers_list) + 1

    #     add_page = addgroup.AddGroup(self.driver)
    #     add_page.navigate_to_page()
    #     add_page.set_name("School number " + str(count))
    #     add_page.select_active(True)
    #     add_page.set_description("This is description for School number " + str(count) + ", added for testing.")
    #     add_page.select_location_by_index(0)
    #     add_page.save_group()

    #     customer_groups_page.navigate_to_page()
    #     find = customer_groups_page.search_for_customer("School number " + str(count))
    #     self.assertNotEqual(find, None, "School number " + str(count))


    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    exit(0)

