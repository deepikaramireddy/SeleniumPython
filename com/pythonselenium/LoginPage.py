#importing webdriver module in selenium package
from selenium import webdriver
from selenium.webdriver.common.by import By

#opening orangehrm login page
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/")


#performing action on username component
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("Admin")

#performing action on password component
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("admin123")

#Clicking the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

#writing test case to verify the title of the page after login
actual_title = driver.title
expected_title = "OrangeHRM"

if actual_title == expected_title:
    print("Test case passed")
else:
    print("Test case failed")
