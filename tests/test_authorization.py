from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver
from data import UsersTestData


class TestAuthenticationButtonLogin:
#Вход по кнопке «Войти в аккаунт» на главной
    def test_authentication_by_button_login_in_main_page_success(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_MAIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_REGISTER))
        driver.find_element(*TestLocators.INPUT_EMAIL_AUTH).send_keys(UsersTestData.email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_AUTH).send_keys(UsersTestData.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_THE_ORDER))
        assert driver.find_element(*TestLocators.BUTTON_MAKE_THE_ORDER).is_displayed()


class TestAuthenticationButtonPersonalAccount:
#Вход через кнопку «Личный кабинет»
    def test_authentication_by_button_personal_account_in_main_page_success(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_REGISTER))
        driver.find_element(*TestLocators.INPUT_EMAIL_AUTH).send_keys(UsersTestData.email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_AUTH).send_keys(UsersTestData.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_THE_ORDER))
        assert driver.find_element(*TestLocators.BUTTON_MAKE_THE_ORDER).is_displayed()


class TestAuthenticationButtonLoginInRegistrationForm:
#Вход через кнопку в форме регистрации
    def test_authentication_by_button_login_in_registration_form_success(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_MAIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_REGISTER))
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_SUBMIT))
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_REGISTRATION_FORM).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_AUTH).send_keys(UsersTestData.email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_AUTH).send_keys(UsersTestData.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_THE_ORDER))
        assert driver.find_element(*TestLocators.BUTTON_MAKE_THE_ORDER).is_displayed()


class TestAuthenticationButtonForgotPassword:
#Вход через кнопку в форме восстановления пароля
    def test_authentication_by_button_forgot_password_in_auth_form_success(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_REGISTER))
        driver.find_element(*TestLocators.BUTTON_FORGOT_PASSWORD).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGIN_PASSWD_RECOVERY_FORM))
        driver.find_element(*TestLocators.BUTTON_LOGIN_PASSWD_RECOVERY_FORM).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_REGISTER))
        driver.find_element(*TestLocators.INPUT_EMAIL_AUTH).send_keys(UsersTestData.email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_AUTH).send_keys(UsersTestData.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_THE_ORDER))
        assert driver.find_element(*TestLocators.BUTTON_MAKE_THE_ORDER).is_displayed()





