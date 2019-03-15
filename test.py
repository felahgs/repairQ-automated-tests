import unittest
from pageobjects.portal import login
from selenium import webdriver


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/portal/org-test-parent/login")

    
    def test_login(self):
        login_page = login.LoginPage(self.driver, 'org-test-parent')
        # login_page.send_username('felipe')
        # login_page.send_password('Testing*123')
        # login_page.select_group(2)
        self.assertTrue(login_page.try_to_login('felipe', 'Test', 2))

    # def tearDown(self):
    #     self.driver.close()

if __name__ == "__main__":
    unittest.main()

