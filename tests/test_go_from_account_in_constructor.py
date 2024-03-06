import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import *
from locators import TestLocators

class TestGoFromAccountInConstructor:
    def test_click_on_link_stellar_burgers(self, driver, url, generated_email, generated_password):
        driver.get(url)

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

        driver.find_element(*TestLocators.MAIN_PAGE_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_LINK_CONSTRUCTOR))

        driver.find_element(*TestLocators.HEADER_LOGO_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_PAGE_ADD_ORDER_BUTTON))

        login_button = driver.find_element(*TestLocators.MAIN_PAGE_ADD_ORDER_BUTTON)
        text = login_button.text

        assert text == "Оформить заказ"


    def test_click_on_link_constructor(self, driver, url, generated_email, generated_password):

        driver.get(url)

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

        driver.find_element(*TestLocators.MAIN_PAGE_PERSONAL_ACCOUNT).click()

        driver.find_element(*TestLocators.HEADER_LINK_CONSTRUCTOR).click()

        login_button = driver.find_element(*TestLocators.MAIN_PAGE_ADD_ORDER_BUTTON)
        text = login_button.text

        assert text == "Оформить заказ"
