import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.fixture
def setup():
    service = Service("C:\\Users\\vaibh\\Downloads\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get(config.get("Url","base_Url"))
    return driver