import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import *
from locators import TestLocators

class TestConstructorSection:
    def test_constructor_sauces(self,  driver):

        element_sauces = driver.find_element(*TestLocators.CONSTRUCTOR_PAGE_ELEMENT_SAUCES)
        driver.execute_script("arguments[0].scrollIntoView();", element_sauces)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.CONSTRUCTOR_PAGE_ELEMENT_SAUCES))

        element_tab = driver.find_element(*TestLocators.CONSTRUCTOR_PAGE_CLICK_TAB)

        assert element_tab.is_displayed()

    def test_constructor_bread(self, driver):

        element_bread = driver.find_element(*TestLocators.CONSTRUCTOR_PAGE_ELEMENT_BREAD)
        driver.execute_script("arguments[0].scrollIntoView();", element_bread)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.CONSTRUCTOR_PAGE_ELEMENT_BREAD))

        element_tab = driver.find_element(*TestLocators.CONSTRUCTOR_PAGE_CLICK_TAB)

        assert element_tab.is_displayed()

    def test_constructor_fillings(self, driver):

        element_fillings = driver.find_element(*TestLocators.CONSTRUCTOR_PAGE_ELEMENT_FILLINGS)
        driver.execute_script("arguments[0].scrollIntoView();", element_fillings)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.CONSTRUCTOR_PAGE_ELEMENT_FILLINGS))

        element_tab = driver.find_element(*TestLocators.CONSTRUCTOR_PAGE_CLICK_TAB)

        assert element_tab.is_displayed()
