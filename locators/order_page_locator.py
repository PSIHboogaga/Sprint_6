from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, '//*[@placeholder="* Имя"]')
    SURNAME_INPUT = (By.XPATH, '//*[@placeholder="* Фамилия"]')
    ADRESS_INPUT = (By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]')
    PHONE_INPUT = (By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]')
    METRO_INPUT = (By.XPATH, '//*[@placeholder="* Станция метро"]')

    METRO_CHERK = (By.XPATH, '//*[contains(text(), "Черкизовская")]')
    BUTTON_NEXT = (By.XPATH, '//button[contains(text(), "Далее")]')
    TIME_FIELD = (By.XPATH, '//*[@placeholder="* Когда привезти самокат"]')
    RENTAL_PERIOD = (By.XPATH, '//*[@class="Dropdown-arrow"]')
    RENTAL_PERIOD_SELECT = (By.XPATH, '//*[contains(text(), "сутки")]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    BUTTON_YES = (By.XPATH, '//button[contains(text(), "Да")]')

    BUTTON_ORDER_UP = (By.XPATH, '//*[@class="Button_Button__ra12g"]')
    BUTTON_ORDER_DOWN = (By.XPATH, '//*[@class="Button_Button__ra12g Button_UltraBig__UU3Lp"]')

    BANNER_ORDER_OK = (By.XPATH, '//*[contains(text(), "Заказ оформлен")]')
