import allure
import pytest
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

options = Options()
options.add_argument("--remote-debugging-port=9222")
# options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)
browser.config.driver = driver



@pytest.fixture(scope='session', autouse=True, name='Работа с браузером')
def browser_management():
    browser.config.base_url = 'https://github.com'
    browser.config.timeout = 2.0
    browser.config.window_width = 1400
    browser.config.window_heigth = 1200

    yield

    with allure.step('Закрываем браузер'):
        browser.quit()

