from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver
from conftest import login


class TestSwitchBlockFillingsLogin:
#Проверка перехода в раздел "Начинки", с логином
    def test_switch_to_fillings_block_success_login(self, driver, login):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_THE_ORDER))
        driver.find_element(*TestLocators.FILLINGS_BLOCK).click()
        assert driver.find_element(*TestLocators.SELECTED_BUTTON).text == "Начинки"


class TestSwitchBlockFillingsLogout:
    # Проверка перехода в раздел "Начинки", без логина
    def test_switch_to_fillings_block_success_logout(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGIN_IN_MAIN))
        driver.find_element(*TestLocators.SAUCES_BLOCK).click()
        driver.find_element(*TestLocators.FILLINGS_BLOCK).click()
        assert driver.find_element(*TestLocators.SELECTED_BUTTON).text == "Начинки"

