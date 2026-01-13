"""
Standalone Selenium demo: handling multiple browser windows.

Demonstrates handling a child browser window, extracting data from it,
switching back to the main window, and validating an intentionally failed
login attempt by asserting the error message.
This script is a negative test scenario by design.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(4)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()

windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])

message = driver.find_element(By.CSS_SELECTOR, ".red").text
email_from_child_window = message.split("at")[1].strip().split(" ")[0]

driver.close()
driver.switch_to.window(windowsOpened[0])

driver.find_element(By.ID, "username").send_keys(email_from_child_window)
driver.find_element(By.ID, "password").send_keys(email_from_child_window)
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))

print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
driver.quit()
