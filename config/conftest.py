import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service


@pytest.fixture()
def browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver

    driver.quit()
