import unittest

from colorama import init, deinit, Fore, Style
from selenium import webdriver

from pageobjects.repairq.customergroups import customergroups
from pageobjects.repairq import login

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        login_page = login.LoginPage(self.driver)
        login_page.navigate_to_page()
        login_page.try_to_login('felipe', 'felipe', 0)
        self.driver.get("https://cinq.repairq.io/customerGroups")

    def test_count_all_children(self):
        groups_page = customergroups.CustomerGroupsPage(self.driver)
        customers_list = groups_page.get_customers()
        # customers = groups_page.get_page_customers()

        for customer in customers_list:
            # Identify number of children (recursively for each children) for the given element
            children_total = groups_page.count_children(customer.get('name'), customers_list)

            # Clicking subgroups buttom
            group_details = groups_page.navigate_to_group_details(customer.get('link'))
            subgroups_count = group_details.count_subgroups()

            # Print result for each group 
            init() # Initialize colorama for coloring output messages ( doesn't )
            print(customer.get('name') + ":", children_total, "children and", subgroups_count, "subgroups", Fore.GREEN + "OK" + Style.RESET_ALL if children_total == subgroups_count else Fore.RED + "ERROR" + Style.RESET_ALL) 
            self.assertEqual(children_total, subgroups_count, "Incorrect number of subgroups for " + customer.get('name'))
            deinit()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    exit(0)

