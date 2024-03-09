import pytest
import random
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def generated_email():
    random_digits = random.randint(100, 999)
    return f"Sergey_Baulin123_{random_digits}@yandex.ru"

@pytest.fixture
def generated_password():
    random_digits = random.randint(0000000, 9999999)
    return random_digits

url = "https://stellarburgers.nomoreparties.site/"