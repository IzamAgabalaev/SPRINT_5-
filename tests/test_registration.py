from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver
from helper import generate_registarion, generate_registration_validation_email, generate_registration_validation_password
from data import UsersTestData


class TestRegistration:
#Проверка регистрации с валидными данными
    def test_registration_new_account_success_submit(self, driver):
        random_email, random_password = generate_registarion()
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_MAIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_REGISTER))
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_SUBMIT))
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(UsersTestData.username)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(random_password)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGIN))
        assert driver.find_element(*TestLocators.BUTTON_REGISTER).is_displayed()


class TestRegistrationNameEmpty:
#Проверка регистрации аккаунта при пустом поле "Имя"
    def test_registration_name_is_empty_failed_submit(self, driver):
        random_email, random_password = generate_registarion()
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_MAIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_REGISTER))
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_SUBMIT))
        driver.find_element(*TestLocators.INPUT_NAME).send_keys('')
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(random_password)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        assert driver.find_element(*TestLocators.BUTTON_SUBMIT).is_displayed()


class TestRegistrationNoEmailDomain:
#Проверка регистрации аккаунта при вводе email без домена.
    def test_registration_invalid_email_without_at_failed_submit(self, driver):
        random_email_no_domain = generate_registration_validation_email()
        random_password = generate_registarion()
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_MAIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_REGISTER))
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_SUBMIT))
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(UsersTestData.username)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(random_email_no_domain)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(random_password)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        assert driver.find_element(*TestLocators.BUTTON_SUBMIT).is_displayed()


class TestRegistrationInvalidLengthPassword:
#Проверка регистрация аккаунта при вводе НЕвалидного по длине значения в поле "Пароль"
    def test_registration_invalid_length_password_failed_submit(self, driver):
        random_email = generate_registarion()
        password_invalid_length = generate_registration_validation_password()
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_MAIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_REGISTER))
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_SUBMIT))
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(UsersTestData.username)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password_invalid_length)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        assert driver.find_element(*TestLocators.BUTTON_SUBMIT).is_displayed()


class TestRegistrationNotificationIncorrectPassword:
# Проверка появления подсказки при вводе НЕвалидного по длине значения в поле "Пароль"
    def test_registration_invalid_length_password_notification_incorrect_password(self, driver):
        email_3, password_invalid_length = generate_registration_validation_password()
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_MAIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_REGISTER))
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_SUBMIT))
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(UsersTestData.username)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email_3)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password_invalid_length)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        assert driver.find_element(*TestLocators.NOTIFICATION_INCORRECT_PASSWORD).text == 'Некорректный пароль'

