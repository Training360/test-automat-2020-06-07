from selenium import webdriver
from selenium.webdriver.common.by import By

from location_page import LocationPage


class TestSimpleTest:

    def test_default(self):
        page = LocationPage()
        page.open_list_screen()
        page.create_location(name="Not default name")
        page.close()


    def test_simple_test(self):
        page = LocationPage()
        page.open_list_screen()
        with open("MOCK_DATA.csv") as f:
            for line in f:
                print(line)
                parts = line.strip().split(",")
                city = parts[0]
                lat = parts[1]
                lon = parts[2]
                page.create_location(city, lat + "," + lon)
        page.close()

