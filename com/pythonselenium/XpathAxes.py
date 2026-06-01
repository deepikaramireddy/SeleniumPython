from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

print("ancestor (tr) contains anchor text:", driver.find_element(By.XPATH, "//table//tr[2]//a/ancestor::tr//a").text)
print("child (from td):", driver.find_element(By.XPATH, "//table//tr[2]//td[1]/child::a").text)
print("descendant-or-self (count anchors):", len(driver.find_elements(By.XPATH, "//table//tr[2]//a/descendant-or-self::a")))
print("following (next tr) anchor:", driver.find_element(By.XPATH, "//table//tr[2]//a/following::tr[1]//a").text)
print("following-sibling (next tr sibling) anchor:", driver.find_element(By.XPATH, "//table//tr[2]//a/ancestor::tr/following-sibling::tr[1]//a").text)
print("preceding (previous tr) anchor:", driver.find_element(By.XPATH, "//table//tr[2]//a/preceding::tr[1]//a").text)
print("preceding-sibling (prev tr sibling) anchor:", driver.find_element(By.XPATH, "//table//tr[2]//a/ancestor::tr/preceding-sibling::tr[1]//a").text)
print("ancestor-or-self tag:", driver.find_element(By.XPATH, "//table//tr[2]//a/ancestor-or-self::tr").tag_name)
print("href (attribute via get_attribute):", driver.get_attribute("href"))

driver.quit()