from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

def test_login(username, password):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

# Test Cases
# TC01 - Valid Credentials
test_login("student", "Password123")

# TC02 - Invalid Password
driver.get("https://practicetestautomation.com/practice-test-login/")
test_login("student", "wrongpass")

# TC03 - Invalid Username
driver.get("https://practicetestautomation.com/practice-test-login/")
test_login("wronguser", "Password123")

# TC04 - Empty Username
driver.get("https://practicetestautomation.com/practice-test-login/")
test_login("", "Password123")

# TC05 - Empty Password
driver.get("https://practicetestautomation.com/practice-test-login/")
test_login("student", "")

# TC06 - Empty Both
driver.get("https://practicetestautomation.com/practice-test-login/")
test_login("", "")

driver.quit()
Add login test script.
