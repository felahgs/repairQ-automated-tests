from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import sys

# Driver Start up
driver = webdriver.Chrome()
driver.get("https://cinq.repairq.io/")

##FUNCTIONS##

# Return the name of the customer
def get_name(element):
    return element.find_elements_by_class_name("wrap-text")[0].get_attribute("innerHTML").strip()

# Return the name of the customer Parent (customer Group)
def get_parent(element):
    return element.find_elements_by_class_name("wrap-text")[2].get_attribute("innerHTML").strip()

# Return the total of children and sub children of a given customer (Total of customers in customer group)
def count_children(element_name):
    # sys.stdout.write('.')   
    count = 0
    childlist = []
    customer_page = driver.current_url
    driver.get("https://cinq.repairq.io/customerGroups")

    # Search for childs in all pages starting in the first one 
    # while(have_next_page()):
    #     for member in customers:
    #         print('element name', element_name)
    #         print('member parent', get_parent(member))
    #         if( element_name == get_parent(member)):
    #             count += 1
    #             childlist.append(get_name(member))

    # Check for every customer on all pages if they are children of the 
    #   selected element
    while True:
        customers = driver.find_elements_by_class_name("largest-row")
        for member in customers:
            # print('element name', element_name)
            # print('member parent', get_parent(member))
            if( element_name == get_parent(member)):
                count += 1
                childlist.append(get_name(member))
        # Click to go another page. If success return true
        # Break loop when there is no more page to go
        if not have_next_page():
            break

    # Call the function recursively for each child
    for child in childlist:
        count = count + count_children(child)

    # Return to the original page where the function was called
    driver.get(customer_page)
    return count

# Check if there is a next page
def have_next_page():
    # print('changing page')
    page_nav = driver.find_element_by_id("yw1")
    next = page_nav.find_element_by_class_name("next")
    link = next.find_element_by_tag_name("a")
    if "disable" not in next.get_attribute("class"):
        link.click()
        return True
    else: 
        return False

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

# page_nav = driver.find_element_by_id("yw1")
# next = page_nav.find_element_by_class_name("next")
# link = next.find_element_by_tag_name("a")
# # print(next.get_attribute("class"))
# # "disable" in next.get_attribute("class")
# print("disable" not in next.get_attribute("class"))

# link.click()
# print(have_next_page())
# print(have_next_page())

# Iteration for every customer in the list
for i in range(0, customers_total):
# for i in range(0, 1):
    # i = 12
    # Fetch the costumers list
    customers = driver.find_elements_by_class_name("largest-row")

    # Assign customer index 
    customer_num = i

    # Get customer name and current url
    customer_name = get_name(customers[customer_num])
    customer_page = driver.current_url
    
    # Identify number of children for the given element
    children_total = count_children(customer_name)

    # # Check if there is entries in the following pages
    # while (have_next_page()):
    #     # print('checking next page')
    #     # print('before', children_total)
    #     customers = driver.find_elements_by_class_name("largest-row")
    #     # print('after', children_total)
    #     # print('count children', count_children(customer_name, customers))
    #     children_total = children_total + count_children(customer_name, customers)

    # # Go back to the customer page
    # driver.get(customer_page)
    # customers = driver.find_elements_by_class_name("largest-row")

    # Clicking costumer details buttom
    customers = driver.find_elements_by_class_name("largest-row")
    show_details = customers[customer_num].find_element_by_class_name("icon-zoom-in")
    show_details.click()

    # Clicking subgroups buttom
    driver.find_element_by_xpath("//a[@href='#subgroups']").click()
    subgroups = driver.find_element_by_id("subgroups")
    subgroups_count = len(subgroups.find_elements_by_class_name("largest-row"))

    # Print test result for this customer
    print(customer_name + ":", children_total, "children and", subgroups_count, "subgroups", "OK" if children_total == subgroups_count else "ERROR") 
    assert(children_total == subgroups_count)

    # Return to the customers page
    driver.get("https://cinq.repairq.io/customerGroups")

    # link = "https://cinq.repairq.io/customerGroups/" + str(customer_num - 1)
    # driver.get(link)

driver.quit()
