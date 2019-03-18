from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://cinq.repairq.io/")


elem = driver.find_element_by_id("UserLoginForm_username")
elem.send_keys("pedro")

elem = driver.find_element_by_id("UserLoginForm_password")
elem.send_keys("pedro")
elem.send_keys(Keys.RETURN)

driver.get("https://cinq.repairq.io/customerGroups")

driver.get("https://cinq.repairq.io/customerGroups/add")



