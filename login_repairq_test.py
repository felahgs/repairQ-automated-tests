import unittest
from pageobjects.repairq import login
from selenium import webdriver


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://cinq.repairq.io/site/login")

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

