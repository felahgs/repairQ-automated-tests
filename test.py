from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pageobjects.repairq.customergroups import customergroups

driver = webdriver.Chrome()
driver.get("https://cinq.repairq.io/")


elem = driver.find_element_by_id("UserLoginForm_username")
elem.send_keys("pedro")

elem = driver.find_element_by_id("UserLoginForm_password")
elem.send__keys("pedro")
elem.send_keys(Keys.RETURN)

driver.get("https://cinq.repairq.io/customerGroups")
# count = len(driver.find_elements_by_class_name("largest-row"))

page = customergroups.CustomerGroupsPage(driver)
customer = page.search_for_customer('Bend Public Schools')
print(customer)
count = page.count_children('Bend Public Schools')
print(count)