from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


from pageobjects.basepage import BasePage

class GroupDetailsPage(BasePage):
    CGROUP_DETAIL_PAGE = (By.ID, "customer-group-controller")
    SUBGROUPS_BTN = (By.XPATH, "//a[@href='#subgroups']")
    SUBGROUPS_LIST = (By.ID, "subgroups")
    SUBGROUP = (By.CLASS_NAME, "largest-row")
    
    # PAGE_NAVIGATION = (By.ID, 'yw2')
    # NEXT_BTN = (By.CLASS_NAME, 'next')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.presence_of_element_located(GroupDetailsPage.CGROUP_DETAIL_PAGE))


    def navigate_to_page(self):
        pass

    def click_subgroups(self):
        button = self.driver.find_element(*GroupDetailsPage.SUBGROUPS_BTN)
        button.click()

    def count_subgroups(self):
        try: 
            self.driver.find_element(*GroupDetailsPage.SUBGROUPS_LIST)
        except NoSuchElementException:
            self.click_subgroups()

        groups_list = self.driver.find_element(*GroupDetailsPage.SUBGROUPS_LIST)
        count = 0
        count += len(groups_list.find_elements(*GroupDetailsPage.SUBGROUP))

        # while True: 
        #     count += len(groups_list.find_elements(*GroupDetailsPage.SUBGROUPS))
        #     if not GroupDetailsPage.have_next_page(self):
        #         break
        
        return count
        
    # def have_next_page(self):
    #     """
    #         Verify if there is a next page of ContactsGroups
            
    #         Args:
    #             driver: Reference to the browser driver

    #         Returns:
    #             True if the next page button is enabled
    #     """
    #     page_nav = self.driver.find_element(*GroupDetailsPage.PAGE_NAVIGATION)
    #     next = page_nav.find_element(*GroupDetailsPage.NEXT_BTN)
    #     link = next.find_element_by_tag_name("a")
    #     if "disable" not in next.get_attribute("class"):
    #         link.click()
    #         return True
    #     else: 
    #         return False