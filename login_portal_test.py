import unittest
from pageobjects.portal import login
from selenium import webdriver


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/portal/org-test-parent/login")

    def test_login_allowed_group(self):
        login_page = login.LoginPage(self.driver, 'org-test-parent')
        self.assertFalse(login_page.try_to_login('tata', 'Testing*123', 1))


    def test_login_not_allowed_group(self):
        login_page = login.LoginPage(self.driver, 'org-test-parent')
        self.assertTrue(login_page.try_to_login('tata', 'Testing*123', 2))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

