import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import *
from locators import TestLocators

class TestLogOutOfAccount:
    def test_click_button_log_out_of_account(self, driver, generated_email, generated_password):

        driver.get(url)

        driver.find_element(*TestLocators.MAIN_PAGE_PERSONAL_ACCOUNT).click()

        driver.find_element(*TestLocators.LOGIN_PAGE_REGISTRATION_FORM_BUTTON).click()

        driver.find_element(*TestLocators.REGISTRATION_PAGE_NAME).send_keys("Sergey")
        driver.find_element(*TestLocators.REGISTRATION_PAGE_EMAIL).send_keys(generated_email)
        driver.find_element(*TestLocators.REGISTRATION_PAGE_PASSWORD).send_keys(generated_password)

        driver.find_element(*TestLocators.REGISTRATION_PAGE_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_PAGE_LOG_IN_BUTTON))

        driver.find_element(*TestLocators.REGISTRATION_PAGE_EMAIL).send_keys(generated_email)
        driver.find_element(*TestLocators.REGISTRATION_PAGE_PASSWORD).send_keys(generated_password)
        driver.find_element(*TestLocators.LOGIN_PAGE_LOG_IN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_PAGE_LOG_IN_BUTTON))

        driver.find_element(*TestLocators.MAIN_PAGE_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_PAGE_LOG_OUT_BUTTON))

        driver.find_element(*TestLocators.LOGIN_PAGE_LOG_OUT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_PAGE_LOG_IN_BUTTON))

        login_button = driver.find_element(*TestLocators.LOGIN_PAGE_LOG_IN_BUTTON)
        text = login_button.text

        assert text == 'Войти'
