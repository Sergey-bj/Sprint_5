from selenium.webdriver.common.by import By

class TestLocators:
    # MAIN_PAGE
    MAIN_PAGE_PERSONAL_ACCOUNT = By.XPATH, './/a[@href="/account"]' # Кнопка Личный кабинет
    MAIN_PAGE_ADD_ORDER_BUTTON = By.XPATH, ".//button[text()='Оформить заказ']"  # Кнопка Оформить заказ
    MAIN_PAGE_LOG_IN_PERSONAL_ACCOUNT_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"  # Кнопка Войти в аккаунт

    # REGISTER_PAGE
    REGISTRATION_PAGE_NAME = By.XPATH, ".//input[@class='text input__textfield text_type_main-default']"   # Поле Имя
    REGISTRATION_PAGE_EMAIL = By.XPATH, ".//label[text()='Email']/following-sibling::input"  # Поле Email
    REGISTRATION_PAGE_PASSWORD = By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name='Пароль']"     # Поле Password
    REGISTRATION_PAGE_BUTTON = By.XPATH, ".//button[text()='Зарегистрироваться']"    # Кнопка Зарегистрироваться
    REGISTRATION_PAGE_ERROR_PASSWORD = By.XPATH, ".//p[text()='Некорректный пароль']"    # Cообщение об ошибке Некорреткный пароль

    # LOGIN_PAGE
    REGISTRATION_PAGE_EMAIL # Поле Email
    REGISTRATION_PAGE_PASSWORD # Поле password
    LOGIN_PAGE_REGISTRATION_FORM_BUTTON = By.XPATH, '//a[@href="/register"]'      # Кнопка Зарегистрироваться переводит на страницу register
    LOGIN_PAGE_LOG_IN_BUTTON = By.XPATH, ".//button[text()='Войти']"   # Кнопка Войти
    LOGIN_PAGE_TEXT_PAGE = By.XPATH, "//h2[@class='']"                             # Заголовок формы "Вход"
    LOGIN_PAGE_LOG_OUT_BUTTON = By.XPATH, ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and text()='Выход']"   # Кнопка Выход
    LOGIN_PAGE_PASSWORD_RECOVERY_FORM = By.XPATH, './/a[@href="/forgot-password"]'  # Ссылка Восстановить пароль
    LOGIN_PAGE_RECOVERY_FORM_LOGIN = By.XPATH, './/a[@href="/login"]'  # Ссылка Войти

    #CONSTRUCTOR_PAGE
    CONSTRUCTOR_PAGE_ELEMENT_SAUCES = By.XPATH, ".//h2[2][@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']"      # Кнопка Соусы
    CONSTRUCTOR_PAGE_ELEMENT_BREAD = By.XPATH, ".//h2[1][@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']"       # Кнопка Булки
    CONSTRUCTOR_PAGE_ELEMENT_FILLINGS = By.XPATH, ".//h2[3][@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']"  # Кнопка Начинки
    CONSTRUCTOR_PAGE_CLICK_TAB = By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"  #Переход на TAB при клике на элементы конструктора "Собери бургер"

    #HEADER
    HEADER_LOGO_BUTTON = By.XPATH, '//div[ contains(@class, "header__logo")]/a'  # кнопка Логотип
    HEADER_LINK_CONSTRUCTOR = By.XPATH, './/li[1]/a[@href="/"]'      # Кнопка Конструктор





