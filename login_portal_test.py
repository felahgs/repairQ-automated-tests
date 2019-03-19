import unittest
from pageobjects.portal import login
from selenium import webdriver


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/portal/org-test-parent/login")

    def test_login_allowed_group(self):
        login_page = login.LoginPage(self.driver, 'org-test-parent')
        self.assertTrue(login_page.try_to_login('tata', 'Testing*123', 1), "Should return True for a successful login")

    def test_login_not_allowed_group(self):
        login_page = login.LoginPage(self.driver, 'org-test-parent')
        self.assertFalse(login_page.try_to_login('tata', 'Testing*123', 2), "Should return True for a NOT successful login")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    exit(0)

