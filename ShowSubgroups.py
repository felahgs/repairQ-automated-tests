from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from colorama import init, deinit, Fore, Style

from pagemethods.customergroups import (get_name, 
                                        get_parent,
                                        count_children,
                                        have_next_page)

import sys

#
# Check if all the schools listed in the customerGroup page 
# are shown in school's subgroups tab 
#

# Driver Start up
driver = webdriver.Chrome()

## Login
driver.get("https://cinq.repairq.io/")
elem = driver.find_element_by_id("UserLoginForm_username")
elem.send_keys("felipe")
elem = driver.find_element_by_id("UserLoginForm_password")
elem.send_keys("felipe")
elem.send_keys(Keys.RETURN)

# Navigate to the customer groups page
driver.get("https://cinq.repairq.io/customerGroups")

# customers = driver.find_elements_by_class_name("largest-row")

# For each page, check the number of child for every customer
while True:
    # Identify quantity of Customer on the Costumers Group Page
    customers_total = len(driver.find_elements_by_class_name("largest-row"))

    # Save page current URL
    customer_page = driver.current_url

    for i in range(0, customers_total):
    # for i in range(0, 1):
        # i = 12

        # Fetch the costumers list
        customers = driver.find_elements_by_class_name("largest-row")

        # Assign customer index 
        customer_num = i

        # Get customer name and current page url
        customer_name = get_name(customers[customer_num])
        customer_page = driver.current_url
        
        # Identify number of children (recursively for each children) for the given element
        children_total = count_children(driver, customer_name)

        # Clicking costumer details buttom
        customers = driver.find_elements_by_class_name("largest-row")
        show_details = customers[customer_num].find_element_by_class_name("icon-zoom-in")
        show_details.click()

        # Clicking subgroups buttom
        driver.find_element_by_xpath("//a[@href='#subgroups']").click()
        subgroups = driver.find_element_by_id("subgroups")
        subgroups_count = len(subgroups.find_elements_by_class_name("largest-row"))

        # Print test result for this customer 
        init() # Initialize colorama for coloring output messages ( doesn't )
        print(customer_name + ":", children_total, "children and", subgroups_count, "subgroups", Fore.GREEN + "OK" + Style.RESET_ALL if children_total == subgroups_count else Fore.RED + "ERROR" + Style.RESET_ALL) 
        assert(children_total == subgroups_count)
        deinit()

        # Return to the customers page
        driver.get(customer_page)
    # Break loop when there is no more page to go
    if not have_next_page(driver):
        break


driver.quit()
