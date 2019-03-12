from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import sys

# Driver Start up
driver = webdriver.Chrome()
driver.get("https://cinq.repairq.io/")

##FUNCTIONS##

# Return the name of the School
def get_name(element):
    return element.find_elements_by_class_name("wrap-text")[0].get_attribute("innerHTML").strip()

# Return the name of the School Parent (School Group)
def get_parent(element):
    return element.find_elements_by_class_name("wrap-text")[2].get_attribute("innerHTML").strip()

# Return the total of children and sub children of a given school (Total of schools in school group)
def count_children(element, customers):
    # sys.stdout.write('.')   
    count = 0
    childlist = []
    for member in customers:
        if( get_name(element) == get_parent(member)):
            count += 1
            childlist.append(member)

    for child in childlist:
        count = count + count_children(child, customers)
    return count
## FUNCTIONS END ##

## Login
elem = driver.find_element_by_id("UserLoginForm_username")
elem.send_keys("felipe")
elem = driver.find_element_by_id("UserLoginForm_password")
elem.send_keys("felipe")
elem.send_keys(Keys.RETURN)

# Navigate to the customer groups page
driver.get("https://cinq.repairq.io/customerGroups")

# customers = driver.find_elements_by_class_name("largest-row")

# Identify quantity of Customer on the Costumers Group Page
customers_total = len(driver.find_elements_by_class_name("largest-row"))


# Iteration for every school in the list
for i in range(0, customers_total):

    # Fetch the costumers list
    customers = driver.find_elements_by_class_name("largest-row")

    # Assign customer index 
    customer_num = i

    # Get customer name
    customer_name = get_name(customers[customer_num])

    # Identify number of children for the given element
    children_total = count_children(customers[customer_num], customers)

    # Clicking costumer details buttom
    show_details = customers[customer_num].find_element_by_class_name("icon-zoom-in")
    show_details.click()

    # Clicking subgroups buttom
    driver.find_element_by_xpath("//a[@href='#subgroups']").click()
    subgroups = driver.find_element_by_id("subgroups")
    subgroups_count = len(subgroups.find_elements_by_class_name("largest-row"))

    # Print test result for this school
    print(customer_name + ":", children_total, "children and", subgroups_count, "subgroups", "OK" if children_total == subgroups_count else "ERROR") 
    assert(children_total == subgroups_count)

    # Return to the customers page
    driver.get("https://cinq.repairq.io/customerGroups")

    # link = "https://cinq.repairq.io/customerGroups/" + str(customer_num - 1)
    # driver.get(link)

driver.quit()
