from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import names
import random

driver = webdriver.Chrome()
driver.get("http://klosowsk.rq.test")


## Login
elem = driver.find_element_by_id("UserLoginForm_username")
elem.send_keys("pedrocunha")
elem = driver.find_element_by_id("UserLoginForm_password")
elem.send_keys("pedro")
elem.send_keys(Keys.RETURN)

## Access Add Customer Group User screen
driver.get("http://klosowsk.rq.test/customerGroupUsers/add")

## Fill necessary attributes
elem = driver.find_element_by_id("CustomerGroupUserForm_first_name")
name = names.get_first_name()
elem.send_keys(name)
elem = driver.find_element_by_id("CustomerGroupUserForm_last_name")
lastname = names.get_last_name()
elem.send_keys(lastname)
elem = driver.find_element_by_id("CustomerGroupUserForm_email")
elem.send_keys(str.lower(name) + "@" + str.lower(lastname) + ".com")
elem = driver.find_element_by_id("CustomerGroupUserForm_pri_phone")
elem.send_keys(random.randint(10000,999999999999))

elem = driver.find_element_by_id("CustomerGroupUserForm_username")
elem.send_keys(str.lower(name))

elem = driver.find_element_by_id("CustomerGroupUserForm_pin")
elem.send_keys("Cinq2019*")
elem = driver.find_element_by_id("CustomerGroupUserForm_confirm_pin")
elem.send_keys("Cinq2019*")


select = Select(driver.find_element_by_id("addCustomerGroup"))
select.select_by_index(1)

elem = driver.find_element_by_id("btnAddGroup")
elem.click()

elem = driver.find_element_by_id("UserForm_3_role_portal_user")
elem.click()
elem = driver.find_element_by_id("UserForm_3_role_portal_admin")
elem.click()



#driver.quit()
