import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
time.sleep(5)

username = driver.find_element(By.ID, "user-name")

password = driver.find_element(By.ID, "password")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
time.sleep(5)

submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-button.btn_action")

submit_button.click()

driver.quit()