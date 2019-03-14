from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from pagemethods.loginorg import login

import names
import random

driver = webdriver.Chrome()
 
## Try to Login with the new user ##
# driver.get('http://localhost:3000/portal/org-test-parent/login')

 # Wait for the page to load
# wait = WebDriverWait(driver, 10)
# elem = wait.until(EC.element_to_be_clickable((By.ID, 'username')))

login(driver,'org-test-parent', 'elizabeth9936', 'Testing*123', 1)
