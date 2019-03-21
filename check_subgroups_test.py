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
        while True:
        # Identify quantity of Customer on the Costumers Group Page
            customers_total = len(self.driver.find_elements_by_class_name("largest-row"))

            # Save page current URL
            initial_page = self.driver.current_url

            for i in range(0, customers_total):
            # for i in range(0, 3):

                # Fetch the costumers list
                customers = groups_page.get_page_customers()

                # Assign customer index 
                customer_num = i

                # Get customer name and current page url
                customer_name = groups_page.get_name(customers[customer_num])
                initial_page = self.driver.current_url
                
                # Identify number of children (recursively for each children) for the given element
                children_total = groups_page.count_children(customer_name)

                # Clicking costumer details buttom
                customers = groups_page.get_page_customers()

                # Clicking subgroups buttom
                group_details = groups_page.navigate_to_group_details(customers[customer_num])
                subgroups_count = group_details.count_subgroups()

                init() # Initialize colorama for coloring output messages ( doesn't )
                print(customer_name + ":", children_total, "children and", subgroups_count, "subgroups", Fore.GREEN + "OK" + Style.RESET_ALL if children_total == subgroups_count else Fore.RED + "ERROR" + Style.RESET_ALL) 
                self.assertEqual(children_total, subgroups_count, "Incorrect number of subgroups for " + customer_name)
                deinit()

                self.driver.get(initial_page)
            if not groups_page.have_next_page():
                break

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    exit(0)

