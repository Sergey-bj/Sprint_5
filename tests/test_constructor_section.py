import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import *
from locators import TestLocators

class TestConstructorSection:
    def test_constructor_sauces(self,  driver):

        driver.get(url)

        element_sauces = driver.find_element(*TestLocators.CONSTRUCTOR_PAGE_ELEMENT_SAUCES)
        driver.execute_script("arguments[0].scrollIntoView();", element_sauces)
        text = element_sauces.text

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.CONSTRUCTOR_PAGE_ELEMENT_SAUCES))

        assert text == 'Соусы'

    def test_constructor_bread(self, driver):

        driver.get(url)

        element_bread = driver.find_element(*TestLocators.CONSTRUCTOR_PAGE_ELEMENT_BREAD)
        driver.execute_script("arguments[0].scrollIntoView();", element_bread)
        text = element_bread.text

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.CONSTRUCTOR_PAGE_ELEMENT_BREAD))

        assert text == 'Булки'

    def test_constructor_fillings(self, driver):

        driver.get(url)

        element_fillings = driver.find_element(*TestLocators.CONSTRUCTOR_PAGE_ELEMENT_FILLINGS)
        driver.execute_script("arguments[0].scrollIntoView();", element_fillings)
        text = element_fillings.text

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.CONSTRUCTOR_PAGE_ELEMENT_FILLINGS))

        assert text == 'Начинки'
