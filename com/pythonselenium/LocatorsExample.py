import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(5)

email = "ramireddydeepika@gmail.com"
pwd = "Deepa@123"

e_id = driver.find_element(By.ID, "_R_1h6kqsqppb6amH1_"); e_id.clear(); e_id.send_keys(email); print("By.ID ->", e_id.get_attribute("id"))
e_name = driver.find_element(By.NAME, "pass"); e_name.clear(); e_name.send_keys(pwd); print("By.NAME ->", e_name.get_attribute("name"))
e_class = driver.find_element(By.CLASS_NAME, "x1i10hfl"); print("By.CLASS_NAME ->", e_class.get_attribute("class"))
e_tag = driver.find_element(By.TAG_NAME, "input");print("By.TAG_NAME ->", e_tag.get_attribute("type"))
l_link = driver.find_element(By.LINK_TEXT, "Forgotten password?");  print("By.LINK_TEXT ->", l_link.text)
p_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot"); print("By.PARTIAL_LINK_TEXT ->", p_link.text)
css_id = driver.find_element(By.CSS_SELECTOR, "#_R_1h6kqsqppb6amH1_");  print("CSS #id ->", css_id.get_attribute("id"))
css_name = driver.find_element(By.CSS_SELECTOR, "input[name='pass']"); print("CSS name ->", css_name.get_attribute("name"))
css_tag_id = driver.find_element(By.CSS_SELECTOR, "input#_R_1h6kqsqppb6amH1_"); print("CSS tag#id ->", css_tag_id.get_attribute("id"))
css_multi = driver.find_element(By.CSS_SELECTOR, "input[type='password'][name='pass']"); print("CSS multi ->", css_multi.get_attribute("name"))
xp_id = driver.find_element(By.XPATH, "//input[@id='_R_1h6kqsqppb6amH1_']"); print("XPATH @id ->", xp_id.get_attribute("id"))
xp_name = driver.find_element(By.XPATH, "//input[@name='pass']");print("XPATH @name ->", xp_name.get_attribute("name"))

driver.quit()