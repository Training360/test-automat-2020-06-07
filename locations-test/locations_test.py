from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\training\\chromedriver.exe")
driver.get("http://localhost:8080/server")
driver.find_element(By.LINK_TEXT, "Create location").click()

driver.find_element(By.ID, "name-input").send_keys("Hello")
driver.find_element(By.ID, "coords-input").send_keys("1,1")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
driver.find_element(By.LINK_TEXT, "Back to list").click()

driver.quit()