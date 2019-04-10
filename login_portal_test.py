import unittest
import time

from pageobjects.portal import login
from pageobjects import root_url
from pageobjects.portal import home

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.get(root_url.portal + "/org-test-parent/login")

    def test_check_groups_list(self):
        login_page = login.LoginPage(self.driver, 'school-number-10')
        login_page.navigate_to_page()

        login_groups = login_page.group_list_itens()

        login_page.try_to_login('fela', 'Testing*123', "School number 11")

        home_page = home.HomePage(self.driver, 'school-number-10')
        navbar = home_page.navbar
        navbar_groups = navbar.get_groups_dropdown_items()

        self.assertEqual(login_groups, navbar_groups)

    # def test_language_change(self):
    #     login_page = login.LoginPage(self.driver, 'school-number-10')
    #     login_page.navigate_to_page()

    #     login_groups = login_page.group_list_itens()

    #     login_page.try_to_login('fela', 'Testing*123', "School number 11")

    #     home_page = home.HomePage(self.driver, 'school-number-10')
    #     navbar = home_page.navbar

    #     navbar.select_lang_by_index(0)
    #     navbar_groups = navbar.get_groups_dropdown_items()

    #     print('login groups', login_groups)
    #     print('navbar groups', navbar_groups)

    #     print(login_groups == navbar_groups)

    def test_login_allowed_group(self):
        login_page = login.LoginPage(self.driver, 'org-test-parent')
        login_page.navigate_to_page()
        self.assertTrue(login_page.try_to_login('tata', 'Testing*123', "Org Test Child 1"), "Should return True for a successful login")


    def test_login_not_allowed_group(self):
        login_page = login.LoginPage(self.driver, 'org-test-parent')
        login_page.navigate_to_page()
        self.assertFalse(login_page.try_to_login('baba', 'Testing*123', "Org Test Child 1"), "Should return True for a NOT successful login")

    def tearDown(self):
        time.sleep(7)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    exit(0)

