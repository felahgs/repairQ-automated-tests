from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://cinq.repairq.io/")


elem = driver.find_element_by_id("UserLoginForm_username")
elem.send_keys("pedro")

elem = driver.find_element_by_id("UserLoginForm_password")
elem.send_keys("pedro")
elem.send_keys(Keys.RETURN)

driver.get("https://cinq.repairq.io/customerGroups")
# count = len(driver.find_elements_by_class_name("largest-row"))

count=5
while count < 23:

    driver.get("https://cinq.repairq.io/customerGroups/add")

    elem = driver.find_element_by_id("CustomerGroup_name")
    elem.send_keys("Org Test Child " + str(count))

    elem = driver.find_element_by_id("CustomerGroup_description")
    elem.send_keys("This is description for School number " + str(count) + ", added for testing.")

    select = Select(driver.find_element_by_id("CustomerGroup_parent_id"))
    select.select_by_index(22)

    elem = driver.find_element_by_id("save-button")
    elem.click()

    count += 1