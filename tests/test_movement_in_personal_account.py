from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver
from conftest import login


class TestMovementInPersonalAccount:
#Проверка перехода по клику на «Личный кабинет»
    def test_movement_from_main_to_personal_account(self, driver, login):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE))
        assert driver.find_element(*TestLocators.ORDER_HISTORY).is_displayed()

