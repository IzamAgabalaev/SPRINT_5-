from selenium.webdriver.common.by import By


class TestLocators:
    # Регистрация аккаунта
    # Поле "Имя"
    INPUT_NAME = By.XPATH, '//label[text()="Имя"]/following-sibling::input'

    # Поле Email
    INPUT_EMAIL = By.XPATH, './/label[text()="Email"]/following-sibling::input'

    # Поле "Пароль"
    INPUT_PASSWORD = By.XPATH, './/input[@name="Пароль"]'

    # Кнопка "Зарегистрироваться"
    BUTTON_SUBMIT = By.XPATH, '//button[text() = "Зарегистрироваться"]'

    # Нотификация при некорректном пароле
    NOTIFICATION_INCORRECT_PASSWORD = By.XPATH, '//p[text() = "Некорректный пароль"]'

    # Кнопка "Войти" в разделе регистрации
    BUTTON_LOGIN_IN_REGISTRATION_FORM = By.XPATH, '//a[text() = "Войти"]'

    # Аутентификация
    # Поле Email
    INPUT_EMAIL_AUTH = By.XPATH, '//label[text()="Email"]/following-sibling::input'

    # Поле "Пароль"
    INPUT_PASSWORD_AUTH = By.XPATH, '//input[@name = "Пароль"]'

    # Кнопка "Войти"
    BUTTON_LOGIN = By.XPATH, '//button[text()="Войти"]'

    # Кнопка "Зарегистрироваться"
    BUTTON_REGISTER = By.XPATH, '//a[text() = "Зарегистрироваться"]'

    # Восстановление пароля
    # Кнопка "Восстановить пароль"
    BUTTON_FORGOT_PASSWORD = By.XPATH, '//a[text() = "Восстановить пароль"]'

    # Кнопка "Войти" в разделе восстановления пароля
    BUTTON_LOGIN_PASSWD_RECOVERY_FORM = By.XPATH, '//a[text() = "Войти"]'

    # Личный кабинет
    # Раздел "Профиль"
    PROFILE = By.XPATH, '//a[@href = "/account/profile"]'

    # Раздел "История заказов"
    ORDER_HISTORY = By.XPATH, '//a[@href = "/account/order-history"]'

    # Кнопка "Выйти"
    BUTTON_LOGOUT = By.XPATH, '//button[@type = "button"]'

    # Главная
    # Кнопка "Войти в аккаунт" на главной странице
    BUTTON_LOGIN_IN_MAIN = By.XPATH, './/button[text() = "Войти в аккаунт"]'

    # Кнопка "Личный кабинет"
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, '//p[text() = "Личный Кабинет"]'

    # Кнопка "Оформить заказ"
    BUTTON_MAKE_THE_ORDER = By.XPATH, '//button[text()="Оформить заказ"]'

    # Кнопка "Конструктор" в хедере страницы
    HEADER_OF_PAGE_CONSTRUCTOR = By.XPATH, '//p[text() = "Конструктор"]'

    # Селектор, помечающий выбранный раздел конструктора как активный
    SELECTED_BUTTON = By.XPATH, ('//div[@class = '
                                 '"tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')

    # Заголовок раздела "Булки" в меню конструктора
    BUNS_BLOCK = By.XPATH, '//span[text() = "Булки"]'

    # Заголовок раздела "Соусы" в меню конструктора
    SAUCES_BLOCK = By.XPATH, '//span[text() = "Соусы"]'

    # Заголовок раздела "Начинки" в меню конструктора
    FILLINGS_BLOCK = By.XPATH, '//span[text() = "Начинки"]'

    # Кликабельный логотип в шапке сайта
    LOGO = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]'
