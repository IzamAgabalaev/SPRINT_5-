from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver
from conftest import login


class TestMovementToConstructor:
    # Проверка перехода из личного кабинета по клику на «Конструктор»
    def test_movement_from_personal_account_to_constructor_by_header_success(self, driver, login):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE))
        driver.find_element(*TestLocators.HEADER_OF_PAGE_CONSTRUCTOR).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_THE_ORDER))
        assert driver.find_element(*TestLocators.BUTTON_MAKE_THE_ORDER).is_displayed()


class TestMovementToConstructorLogo:
# Проверка перехода из личного кабинета по клику на лого
    def test_movement_from_personal_account_to_constructor_by_logo_success(self, driver, login):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE))
        driver.find_element(*TestLocators.LOGO).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_THE_ORDER))
        assert driver.find_element(*TestLocators.BUTTON_MAKE_THE_ORDER).is_displayed()

