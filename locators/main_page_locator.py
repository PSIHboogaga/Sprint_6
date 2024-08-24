from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_ORDER_UP = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/button[1]')
    BUTTON_ORDER_DOWN = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div[2]/div[5]/button')

    BUTTON_How_much_does_it_cost = (By.XPATH, '//*[@id="accordion__heading-0"]')
    BUTTON_I_want_several_scooters_at_once = (By.XPATH, '//*[@id="accordion__heading-1"]')
    BUTTON_How_is_rental_time_calculated = (By.XPATH, '//*[@id="accordion__heading-2"]')
    BUTTON_Is_it_possible_to_order_a_scooter_directly_for_today = (By.XPATH, '//*[@id="accordion__heading-3"]')
    BUTTON_Is_it_possible_to_extend_the_order_or_return_the_scooter_earlier = (By.XPATH, '//*[@id="accordion__heading-4"]')
    BUTTON_Do_you_bring_a_charger_along_with_the_scooter = (
    By.XPATH, '//*[@id="accordion__heading-5"]')
    BUTTON_Is_it_possible_to_cancel_an_order = (By.XPATH, '//*[@id="accordion__heading-6"]')
    BUTTON_I_live_outside_the_MKAD = (By.XPATH, '//*[@id="accordion__heading-7"]')

    LOGO_SCOOTER = (By.XPATH, '//*[@alt="Scooter"]')
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    FAQ_BUTTONS = (By.CSS_SELECTOR, '.accordion__control')
    FAQ_ANSWERS = (By.CSS_SELECTOR, '.accordion__panel')
