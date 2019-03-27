import unittest
import time

from selenium import webdriver

from pageobjects.repairq import login
from pageobjects.repairq.customergroups import addgroup
from pageobjects.repairq.customergroups import customergroups
from pageobjects import root_url


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        login_page = login.LoginPage(self.driver)
        login_page.navigate_to_page()
        login_page.try_to_login('felipe', 'felipe', 0)
        self.driver.get( root_url.repairq + "/customerGroups/add")

    def test_add_parent_group(self):
        customer_groups_page = customergroups.CustomerGroupsPage(self.driver)
        customer_groups_page.navigate_to_page()
        customers_list = customer_groups_page.get_customers()
        count = len(customers_list) + 1

        add_page = addgroup.AddGroup(self.driver)
        add_page.navigate_to_page()
        add_page.set_name("School number " + str(count))
        add_page.select_active(True)
        add_page.set_description("This is description for School number " + str(count) + ", added for testing.")
        add_page.select_location_by_index(0)
        add_page.save_group()

        customer_groups_page.navigate_to_page()
        find = customer_groups_page.search_for_customer("School number " + str(count))
        self.assertNotEqual(find, None, "School number " + str(count))

    def test_add_child_group(self):
        customer_groups_page = customergroups.CustomerGroupsPage(self.driver)
        customer_groups_page.navigate_to_page()
        count = len(customer_groups_page.get_customers()) + 1

        add_page = addgroup.AddGroup(self.driver)
        add_page.navigate_to_page()
        add_page.set_name("School number " + str(count))
        add_page.set_description("This is description for School number " + str(count) + ", added for testing.")
        add_page.select_active(False)
        add_page.select_location_by_index(1)
        add_page.select_parent_by_text("School number " + str(count-1))
        add_page.save_group()

        customer_groups_page.navigate_to_page()
        school = customer_groups_page.search_for_customer("School number " + str(count))
        self.assertEqual(school.get("parent"), "School number " + str(count-1))


    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    exit(0)

