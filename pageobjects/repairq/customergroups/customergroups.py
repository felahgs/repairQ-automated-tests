from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from pageobjects.basepage import BasePage
from pageobjects.repairq.customergroups import groupdetails


class CustomerGroupsPage(BasePage):
    CUSTOMER_GROUP_PAGE = (By.CLASS_NAME, 'c-customerGroups')
    CUSTOMER_GROUP = (By.CLASS_NAME, 'largest-row') 
    PAGE_NAVIGATION = (By.ID, 'yw2')
    NEXT_BTN = (By.CLASS_NAME, 'next')
    CGROUP_DETAILS_BTN = (By.CLASS_NAME, 'icon-zoom-in')

    def __init__(self, driver):
        self.driver = driver
        self.URL = 'https://cinq.repairq.io/customerGroups'
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.presence_of_element_located(CustomerGroupsPage.CUSTOMER_GROUP_PAGE))


    def navigate_to_page(self):
        self.driver.get(self.URL)
        self.wait.until(EC.element_to_be_clickable(CustomerGroupsPage.CUSTOMER_GROUP_PAGE))

    def get_page_customers(self):
        return self.driver.find_elements(*CustomerGroupsPage.CUSTOMER_GROUP)


    def get_name(self, element):
        """
            Get element name from Customer Group list

            Args:
                element: Customer element from the customer group list.

            Returns:
                innerHTML from the name tag of the selected elemenet
        """
        return element.find_elements_by_class_name("wrap-text")[0].get_attribute("innerHTML").strip()

    def get_parent(self, element):
        """
            Get the name of the element parent  from Customer Group list
            
            Args:
                element: Customer element from the customer group list.

            Returns:
                innerHTML from the parent tag of the selected elemenet
        """
        return element.find_elements_by_class_name("wrap-text")[2].get_attribute("innerHTML").strip()

    def click_cgroup_details(self, element):
        button = element.find_element(*CustomerGroupsPage.CGROUP_DETAILS_BTN)
        button.click()

    def navigate_to_group_details(self, element) -> groupdetails.GroupDetailsPage:
        self.click_cgroup_details(element)
        group_details = groupdetails.GroupDetailsPage(self.driver)
        return group_details

    def have_next_page(self):
        """
            Verify if there is a next page of ContactsGroups
            
            Args:
                driver: Reference to the browser driver

            Returns:
                True if the next page button is enabled
        """
        page_nav = self.driver.find_element(*CustomerGroupsPage.PAGE_NAVIGATION)
        next = page_nav.find_element(*CustomerGroupsPage.NEXT_BTN)
        link = next.find_element_by_tag_name("a")
        if "disable" not in next.get_attribute("class"):
            link.click()
            return True
        else: 
            return False

    def count_customers(self) -> int:
        """
            Count of every customer shown in the Customer Groups page
            
            Args:
                driver: Reference to the browser driver

            Returns:
                Total of elements counted from every page

            Usage: count = count_customers(driver)
        """
        count = 0
        while True: 
            count += len(self.driver.find_elements(*CustomerGroupsPage.CUSTOMER_GROUP))
            if not CustomerGroupsPage.have_next_page(self):
                break
        return count
    
    def count_children(self, element_name):
        """
            Count of every child and descendents from the Customer Groups page
            
            Args:
                driver: Reference to the browser driver
                element_name: String with the Customer 

            Returns:
                Total of elements counted from every page

            Usage: count = count_children(driver, 'Main School')
        """
        count = 0
        childlist = []
        customer_page = self.driver.current_url
        self.driver.get("https://cinq.repairq.io/customerGroups")

        # Check for every customer on all pages if they are children of the 
        #   selected element
        while True: 
            customers = self.driver.find_elements_by_class_name("largest-row")
            for member in customers:
                if( element_name == CustomerGroupsPage.get_parent(self, member)):
                    count += 1
                    childlist.append(CustomerGroupsPage.get_name(self, member))
            # Continue checking in all pages for children
            if not CustomerGroupsPage.have_next_page(self):
                break

        # Call the function recursively for each child of the 
        for child in childlist:
            count = count + CustomerGroupsPage.count_children(self, child)

        # Return to the original page where the function was called
        self.driver.get(customer_page)
        return count

## Check if there is a next page. Return true if the 'next' button is enable ##
