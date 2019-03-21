import unittest
import time

from selenium import webdriver

from pageobjects.repairq import login
from pageobjects.repairq.customergroups import addgroup
from pageobjects.repairq.customergroups import customergroups


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        login_page = login.LoginPage(self.driver)
        login_page.navigate_to_page()
        login_page.try_to_login('felipe', 'felipe', 0)
        self.driver.get("https://cinq.repairq.io/customerGroups/add")

    def test_add_parent_group(self):
        customer_groups_page = customergroups.CustomerGroupsPage(self.driver)
        customer_groups_page.navigate_to_page()
        count = customer_groups_page.count_customers() + 1

        add_page = addgroup.AddGroup(self.driver)
        add_page.navigate_to_page()
        add_page.set_name("School number " + str(count))
        add_page.select_active(True)
        add_page.set_description("This is description for School number " + str(count) + ", added for testing.")
        add_page.select_location(0)
        add_page.save_group()

    def test_add_child_group(self):
        customer_groups_page = customergroups.CustomerGroupsPage(self.driver)
        customer_groups_page.navigate_to_page()
        count = customer_groups_page.count_customers() + 1

        add_page = addgroup.AddGroup(self.driver)
        add_page.navigate_to_page()
        add_page.set_name("School number " + str(count))
        add_page.set_description("This is description for School number " + str(count) + ", added for testing.")
        add_page.select_active(False)
        add_page.select_location(1)
        add_page.select_parent(2)
        add_page.save_group()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    exit(0)

