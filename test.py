from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from pagemethods.customergroups import get_name, get_parent, count_customers

driver = webdriver.Chrome()
 
## Login
driver.get("https://cinq.repairq.io/login")
elem = driver.find_element_by_id("UserLoginForm_username")
elem.send_keys("felipe")
elem = driver.find_element_by_id("UserLoginForm_password")
elem.send_keys("felipe")
elem.send_keys(Keys.RETURN)

## Navigate to the customer groups page
driver.get("https://cinq.repairq.io/customerGroups")

## Print the total number of customers on every page
customers = driver.find_elements_by_class_name("largest-row")
print('Total Customers:', count_customers(driver))

## Get customer name
# customer_name = get_name(customers[0])
# print(customer_name)
