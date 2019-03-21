import unittest
import time
import names
import random

from selenium import webdriver

from pageobjects.repairq import login
from pageobjects.repairq.customergroups import adduser


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        login_page = login.LoginPage(self.driver)
        login_page.navigate_to_page()
        login_page.try_to_login('felipe', 'felipe', 0)
        self.driver.get("https://cinq.repairq.io/customerGroupUsers/add")

    def test_add_user(self):
        name = names.get_first_name()
        lastname = names.get_last_name()
        username = (str.lower(name) + str(random.randint(0,9)) + str(random.randint(000, 999)))
        email = str.lower(name) + "@" + str.lower(lastname) + ".com"
        phone = random.randint(10000,999999999999)
        password = "Testing*123"


        add_page = adduser.AddUser(self.driver)
        add_page.set_first_name(name)
        add_page.set_last_name(lastname)
        add_page.set_email(email)
        add_page.set_phone(phone)
        add_page.set_username(username)
        add_page.set_password(password)
        add_page.set_password_confirmation(password)
        add_page.select_customer_group(1)
        add_page.select_customer_group(3)
        add_page.select_customer_group(6)
        add_page.select_customer_group(7)
        add_page.select_customer_group(8)
        add_page.select_customer_group(9)
        add_page.select_customer_group(10)
        # add_page.select_customer_group(5)
        add_page.set_role_organization_admin(0)
        add_page.set_role_setting_manager(1)
        add_page.set_role_staff_manager(2)
        add_page.set_role_asset_manager(3)
        add_page.set_role_member_manager(4)
        add_page.set_role_service_manager(5)
        add_page.set_role_service_manager(6)
        add_page.save_contact()

    def tearDown(self):
        time.sleep(20)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    exit(0)

