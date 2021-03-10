import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
    driver.implicitly_wait(50)
    print("Launching chrome")

    return driver
