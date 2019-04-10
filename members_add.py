import unittest
import time
import names
import random

from pageobjects.portal import login
from pageobjects import root_url
from pageobjects.portal.members import add_member


from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(root_url.portal + "/org-test-parent/login")
        login_page = login.LoginPage(self.driver, 'org-test-parent')
        login_page.navigate_to_page()
        login_page.try_to_login('tata', 'Testing*123', "Org Test Child 1")


    def test_add_members(self):

        def add_random_members(quantity):
            for i in range(0, quantity):
                name = names.get_first_name()
                lastname = names.get_last_name() 
                email = (str.lower(name) + str(random.randint(0,9)) + str(random.randint(0,9))) + "@" + str.lower(lastname) + ".com"
                phone = random.randint(10000,999999999999)

                members_page = add_member.AddMemberPage(self.driver, 'org-test-parent')
                members_page.navigate_to_page()
                navbar = members_page.navbar

                new_member = {
                    "first_name": name,
                    "last_name": lastname,
                    "email": email,
                    "phone": phone
                }

                members_page.add_new_member(new_member)
        add_random_members(25)

    #     print("table len", len(assets_page.get_assets_elements()))
    #     print('Manufacturer:', assets_page.get_element_manufacturer(assets_page.get_assets_elements()[1]))
    #     print('Model:', assets_page.get_element_model(assets_page.get_assets_elements()[1]))
    #     print('Type:', assets_page.get_element_type(assets_page.get_assets_elements()[1]))
    #     print('School', assets_page.get_element_group(assets_page.get_assets_elements()[1]))
    #     print('Member', assets_page.get_element_member(assets_page.get_assets_elements()[1]))

    #     print(assets_page.get_assets_list_items())

    def tearDown(self):
        time.sleep(7)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    exit(0)

