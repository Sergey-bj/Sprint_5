import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import *
from locators import TestLocators

class TestLogInToAccount:
    def test_authorization_with_button_from_registration_form(self, driver, generated_email, generated_password):

        driver.find_element(*TestLocators.MAIN_PAGE_PERSONAL_ACCOUNT).click()

        driver.find_element(*TestLocators.LOGIN_PAGE_REGISTRATION_FORM_BUTTON).click()

        driver.find_element(*TestLocators.REGISTRATION_PAGE_NAME).send_keys("Sergey")
        driver.find_element(*TestLocators.REGISTRATION_PAGE_EMAIL).send_keys(generated_email)
        driver.find_element(*TestLocators.REGISTRATION_PAGE_PASSWORD).send_keys(generated_password)

        driver.find_element(*TestLocators.REGISTRATION_PAGE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_PAGE_LOG_IN_BUTTON))

        driver.find_element(*TestLocators.REGISTRATION_PAGE_EMAIL).send_keys(generated_email)
        driver.find_element(*TestLocators.REGISTRATION_PAGE_PASSWORD).send_keys(generated_password)
        driver.find_element(*TestLocators.LOGIN_PAGE_LOG_IN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_PAGE_ADD_ORDER_BUTTON))

        login_button = driver.find_element(*TestLocators.MAIN_PAGE_ADD_ORDER_BUTTON)
        text = login_button.text

        assert text == "Оформить заказ"

    def test_authorization_with_button_from_password_recovery_form(self, driver, generated_email, generated_password):

        driver.find_element(*TestLocators.MAIN_PAGE_PERSONAL_ACCOUNT).click()

        driver.find_element(*TestLocators.LOGIN_PAGE_PASSWORD_RECOVERY_FORM).click()

        driver.find_element(*TestLocators.LOGIN_PAGE_RECOVERY_FORM_LOGIN).click()

        driver.find_element(*TestLocators.REGISTRATION_PAGE_EMAIL).send_keys('admin@ya.ru')
        driver.find_element(*TestLocators.REGISTRATION_PAGE_PASSWORD).send_keys('123456789')

        driver.find_element(*TestLocators.LOGIN_PAGE_LOG_IN_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_PAGE_ADD_ORDER_BUTTON))

        login_button = driver.find_element(*TestLocators.MAIN_PAGE_ADD_ORDER_BUTTON)
        text = login_button.text

        assert text == "Оформить заказ"

    def test_authorization_with_button_from_personal_acoount(self, driver, generated_email, generated_password):

        driver.find_element(*TestLocators.MAIN_PAGE_PERSONAL_ACCOUNT).click()

        driver.find_element(*TestLocators.LOGIN_PAGE_REGISTRATION_FORM_BUTTON).click()

        driver.find_element(*TestLocators.REGISTRATION_PAGE_NAME).send_keys("Sergey")
        driver.find_element(*TestLocators.REGISTRATION_PAGE_EMAIL).send_keys(generated_email)
        driver.find_element(*TestLocators.REGISTRATION_PAGE_PASSWORD).send_keys(generated_password)

        driver.find_element(*TestLocators.REGISTRATION_PAGE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_PAGE_LOG_IN_BUTTON))

        driver.find_element(*TestLocators.REGISTRATION_PAGE_EMAIL).send_keys(generated_email)
        driver.find_element(*TestLocators.REGISTRATION_PAGE_PASSWORD).send_keys(generated_password)
        driver.find_element(*TestLocators.LOGIN_PAGE_LOG_IN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_PAGE_ADD_ORDER_BUTTON))

        login_button = driver.find_element(*TestLocators.MAIN_PAGE_ADD_ORDER_BUTTON)
        text = login_button.text

        assert text == "Оформить заказ"

    def test_authorization_with_button_log_in_personal_acoount_main_page(self, driver, generated_email, generated_password):

        driver.find_element(*TestLocators.MAIN_PAGE_LOG_IN_PERSONAL_ACCOUNT_BUTTON).click()

        driver.find_element(*TestLocators.REGISTRATION_PAGE_EMAIL).send_keys('admin@ya.ru')
        driver.find_element(*TestLocators.REGISTRATION_PAGE_PASSWORD).send_keys('123456789')
        driver.find_element(*TestLocators.LOGIN_PAGE_LOG_IN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_PAGE_ADD_ORDER_BUTTON))

        login_button = driver.find_element(*TestLocators.MAIN_PAGE_ADD_ORDER_BUTTON)
        text = login_button.text

        assert text == "Оформить заказ"

