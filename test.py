import time

import chromedriver_binary
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    print('start fixture')
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    print('end fixture')


def test_foo(driver):
    driver.get('https://www.google.com/')
    time.sleep(3)
    search_box = driver.find_element_by_name("q")
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(3)

def test_bar(driver):
    pass
