import pytest
from selenium import webdriver
from locators import TestLocators
from data import UsersTestData


#Фикстура вебдрайвера
@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1200,1080')
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


#Фикстура для авторизации
@pytest.fixture
def login(driver):
    driver.find_element(*TestLocators.BUTTON_LOGIN_IN_MAIN).click()
    driver.find_element(*TestLocators.INPUT_EMAIL_AUTH).send_keys(UsersTestData.email)
    driver.find_element(*TestLocators.INPUT_PASSWORD_AUTH).send_keys(UsersTestData.password)
    driver.find_element(*TestLocators.BUTTON_LOGIN).click()