from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from pageobjects import root_url
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
        self.URL = root_url.repairq + '/customerGroups'
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.presence_of_element_located(CustomerGroupsPage.CUSTOMER_GROUP_PAGE))

    def navigate_to_page(self):
        """
            Navigate to the page of this pageObject

            Returns:
                None
        """
        self.driver.get(self.URL)
        self.wait.until(EC.element_to_be_clickable(CustomerGroupsPage.CUSTOMER_GROUP_PAGE))


    def get_page_customers(self):
        """
            Get every member of the customers groups table from the current page loaded on the
            browser driver. The reference is lost if the page is changed.

            Args:
                None

            Returns:
                An list with a reference for each element
        """
        return self.driver.find_elements(*CustomerGroupsPage.CUSTOMER_GROUP)


    def get_customers(self):
        """
            Return a list of libraries where each element contains one customer group with 'name', parent', 'active' and 'link'

            Args:
                None

            Returns:
                A list of libraries
        """
        self.navigate_to_page()
        customer_list=[]
        while True:
            page_customer = [{
                'name': self.get_name(customer), 
                'parent':self.get_parent(customer),
                'active':self.get_active(customer),
                'link':self.get_details_link(customer)
            } for customer in self.get_page_customers()]
            customer_list = page_customer + customer_list
            if not CustomerGroupsPage.have_next_page(self):
                break
        self.navigate_to_page()
        return customer_list
    

    def search_for_customer(self, name):
        """
            Search for a Customer group by it's name on the customer groups page

            Args:
                name: Name of the customer group

            Returns:
                A python library with the customer group if it is found and a library populated with 'None' otherwise
        """
        customers_list = self.get_customers()
        return next((customer for customer in customers_list if customer.get('name') == name), {'name': None, 'parent':None, 'active': None, 'link': None })


    def get_name(self, element):
        """
            Get element name from Customer Group element

            Args:
                element: Customer web element from the customer group list.

            Returns:
                A string with innerHTML from the name tag of the selected elemenet
        """
        return element.find_elements_by_class_name("wrap-text")[0].get_attribute("innerHTML").strip()


    def get_parent(self, element):
        """
            Get the name of the element parent  from Customer Group element
            
            Args:
                element: Customer web element from the customer group list.

            Returns:
                A string with innerHTML from the parent tag of the selected elemenet
        """
        return element.find_elements_by_class_name("wrap-text")[2].get_attribute("innerHTML").strip()


    def get_active(self, element):
        """
            Get the active status of the element parent  from Customer Group element
            
            Args:
                element: Customer web element from the customer group list.

            Returns:
                A string with the innerHTML from the parent tag of the selected elemenet
        """
        return element.find_elements_by_class_name("wrap-text")[1].get_attribute("innerHTML").strip()


    def get_details_link(self, element):
        """
            Get the link to the destails page of the Customer Group element
            
            Args:
                element: Customer web element from the customer group list.

            Returns:
                A string with the selected customer group 
        """
        tag = element.find_elements_by_class_name("btn-action")[0]
        return tag.get_attribute("href")


    def navigate_to_group_details(self, link) -> groupdetails.GroupDetailsPage:
        """
            Navigate to a customer group details page and return a new page objetect for the page
            
            Args:
                link: A string with the URL of the customer group

            Returns:
                A page object for the customer group details page
        """
        self.driver.get(link)
        group_details = groupdetails.GroupDetailsPage(self.driver)
        return group_details


    def have_next_page(self):
        """
            Verify if there is a next page of ContactsGroups
            
            Args:
                None

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


    def count_children(self, element_name, customers):
        """
            Get the link to the destails page of the Customer Group element
            
            Args:
                element: Customer web element from the customer group list.

            Returns:
                A string with the selected customer group 
        """
        count = 0
        childlist = [customer for customer in customers if customer.get('parent') == element_name]
        count = len(childlist)
        # Call the function recursively for each child in the list (Customer group childs and descendents)
        for child in childlist:
            count = count + CustomerGroupsPage.count_children(self, child.get('name'), customers)
        return count
    