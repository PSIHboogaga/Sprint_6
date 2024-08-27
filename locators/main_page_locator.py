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
    LOGO_YANDEX = (By.XPATH, '//*[@href="//yandex.ru"]') #(By.XPATH, '//*[@alt="Yandex"]')  #(By.CLASS_NAME, 'Header_LogoYandex__3TSOI')

    #FAQ_BUTTONS = (By.CSS_SELECTOR, '.accordion__control')
    #FAQ_ANSWERS = (By.CSS_SELECTOR, '.accordion__panel')


    FAQ_BUTTONS = (By.XPATH, '//*[@id="accordion__heading-"]')
    FAQ_ANSWERS = (By.XPATH, '//*[@id="accordion__panel-"]')


class QuestionLocators:
    QUESTION_0 = (By.XPATH, '//*[@id="accordion__heading-0"]')  # Локатор для вопроса 0
    QUESTION_1 = (By.XPATH, '//*[@id="accordion__heading-1"]')  # Локатор для вопроса 1
    QUESTION_2 = (By.XPATH, '//*[@id="accordion__heading-2"]')  # Локатор для вопроса 2
    QUESTION_3 = (By.XPATH, '//*[@id="accordion__heading-3"]')  # Локатор для вопроса 3
    QUESTION_4 = (By.XPATH, '//*[@id="accordion__heading-4"]')  # Локатор для вопроса 4
    QUESTION_5 = (By.XPATH, '//*[@id="accordion__heading-5"]')  # Локатор для вопроса 5
    QUESTION_6 = (By.XPATH, '//*[@id="accordion__heading-6"]')  # Локатор для вопроса 6
    QUESTION_7 = (By.XPATH, '//*[@id="accordion__heading-7"]')  # Локатор для вопроса 7

class AnswerLocators:
    ANSWER_0 = (By.XPATH, '//*[@id="accordion__panel-0"]')  # Локатор для ответа 0
    ANSWER_1 = (By.XPATH, '//*[@id="accordion__panel-1"]')  # Локатор для ответа 1
    ANSWER_2 = (By.XPATH, '//*[@id="accordion__panel-2"]')  # Локатор для ответа 2
    ANSWER_3 = (By.XPATH, '//*[@id="accordion__panel-3"]')  # Локатор для ответа 3
    ANSWER_4 = (By.XPATH, '//*[@id="accordion__panel-4"]')  # Локатор для ответа 4
    ANSWER_5 = (By.XPATH, '//*[@id="accordion__panel-5"]')  # Локатор для ответа 5
    ANSWER_6 = (By.XPATH, '//*[@id="accordion__panel-6"]')  # Локатор для ответа 6
    ANSWER_7 = (By.XPATH, '//*[@id="accordion__panel-7"]')  # Локатор для ответа 7
