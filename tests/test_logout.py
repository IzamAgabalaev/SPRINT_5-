from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver
from conftest import login

class TestLogout:
    # вход по кнопке «Войти в аккаунт» на главной
    def test_logout_of_personal_account_success(self, driver, login):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_THE_ORDER))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE))
        driver.find_element(*TestLocators.BUTTON_LOGOUT).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGIN))
        assert driver.find_element(*TestLocators.BUTTON_LOGIN).is_displayed()