import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import *
from locators import TestLocators


class TestClickButtonPersonalAccount:
    def test__click_button_personal_account(self, driver, url):

        driver.get(url)

        driver.find_element(*TestLocators.MAIN_PAGE_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_PAGE_LOG_IN_BUTTON)))

        login_button = driver.find_element(*TestLocators.LOGIN_PAGE_LOG_IN_BUTTON)
        text = login_button.text

        assert text == 'Войти'


