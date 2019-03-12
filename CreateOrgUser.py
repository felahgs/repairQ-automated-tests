from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import names
import random

driver = webdriver.Chrome()
driver.get("https://cinq.repairq.io/site/login")

## Login ##
elem = driver.find_element_by_id("UserLoginForm_username")
elem.send_keys("felipe")
elem = driver.find_element_by_id("UserLoginForm_password")
elem.send_keys("felipe")
elem.send_keys(Keys.RETURN)


########### Create a new user for the organization ###########

driver.get("https://cinq.repairq.io/customerGroupUsers/add")

 # Fill necessary attributes with a random name generator library
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
username = (str.lower(name) + str(random.randint(0,9)) + str(random.randint(000, 999)))
elem.send_keys(str.lower(username))

elem = driver.find_element_by_id("CustomerGroupUserForm_pin")
password="Testing*123"
elem.send_keys(password)

elem = driver.find_element_by_id("CustomerGroupUserForm_confirm_pin")
elem.send_keys(password)

## Add customer groups from dropdown ##
select = Select(driver.find_element_by_id("addCustomerGroup"))
select.select_by_visible_text("Org Test Parent")
elem = driver.find_element_by_id("btnAddGroup")
elem.click()
select.select_by_visible_text("  Org Test Child 1")
elem.click()

## Collect the id from the selected groups ##
table = driver.find_element_by_id("roles-table-body")
elements = table.find_elements_by_xpath("*")
id_1 = elements[1].get_attribute("data-group-id")
id_2 = elements[2].get_attribute("data-group-id")

## Mark some roles for the Parent customer group ##
elem = driver.find_element_by_id("UserForm_" + id_1 + "_role_portal_setting_manager")
elem.click()
elem = driver.find_element_by_id("UserForm_" + id_1 + "_role_portal_admin")
elem.click()

## Mark some roules for the Child customer group ##
elem = driver.find_element_by_id("UserForm_" + id_2 + "_role_portal_user")
elem.click()
elem = driver.find_element_by_id("UserForm_" + id_2 + "_role_portal_admin")
elem.click()
elem = driver.find_element_by_id("UserForm_" + id_2 + "_role_portal_service_manager")
elem.click()

## Save contact ##
btn = driver.find_element_by_xpath("//button[text()='Save']")
btn.click()
######### END OF THE USER CREATION #########

print(username)
print(lastname)

## Try to Login with the new user ##
driver.get('http://localhost:3000/portal/org-test-parent/login')

 # Wait for the page to load
wait = WebDriverWait(driver, 10)
elem = wait.until(EC.element_to_be_clickable((By.ID, 'username')))

 # Fill the login fields
elem = driver.find_element_by_id("username")
elem.send_keys(username)
elem = driver.find_element_by_id("password")
elem.send_keys(password)

# Try to log in an unregistered group
select = Select(driver.find_element_by_id("group"))
select.select_by_index(1) 
btn = driver.find_element_by_xpath("//button[text()='Log in']")
btn.click()

# elem = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'username')))
try:
    error = driver.find_element_by_class_name('login-error-ywrapper')
except NoSuchElementException:
    print('Success')
else:
    print('Error Page')

# driver.quit()
# selenium.common.exceptions