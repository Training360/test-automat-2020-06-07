from selenium import webdriver
from selenium.webdriver.common.by import By

class LocationPage():


    def open_list_screen(self):
        self.driver = webdriver.Chrome("C:\\training\\chromedriver.exe")
        self.driver.get("http://localhost:8080/server")

    def create_location(self, name = "Default name", coords = "1,1"):
        self.driver.find_element(By.LINK_TEXT, "Create location").click()
        # self.driver.find_element(By.ID, "name-input").click()
        self.driver.find_element(By.ID, "name-input").send_keys(name)
        # self.driver.find_element(By.ID, "coords-input").click()
        self.driver.find_element(By.ID, "coords-input").send_keys(coords)
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # assert self.driver.find_element(By.CSS_SELECTOR, ".alert").text == "Location has been created."
        self.driver.find_element(By.LINK_TEXT, "Back to list").click()

    def close(self):
        self.driver.close()