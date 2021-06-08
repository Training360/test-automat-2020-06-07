from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome("C:\Java\chromedriver.exe")

driver = webdriver.Remote(
   command_executor='http://localhost:4444/wd/hub',
   desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True})


driver.get("https://www.python.org")

driver.quit()