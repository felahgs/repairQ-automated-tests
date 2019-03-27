import unittest

from pageobjects.repairq import login
from pageobjects import root_url

from selenium import webdriver


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(root_url.repairq + "/site/login")

    def test_login_registered(self):
        login_page = login.LoginPage(self.driver)
        self.assertTrue(login_page.try_to_login('felipe', 'felipe', 0))

    def test_login_unregistered_user(self):
        login_page = login.LoginPage(self.driver)
        self.assertFalse(login_page.try_to_login('unregistereduser', 'pass', 0))


    # def test_login_not_allowed_group(self):

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

