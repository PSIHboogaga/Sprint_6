import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locator import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.description('Клик кнопки заказать(вверху\внизу)')
    def click_order_button(self, index):
        order_button = MainPageLocators.BUTTON_ORDER_UP if index == 0 else MainPageLocators.BUTTON_ORDER_DOWN
        self.wait_and_find_element(order_button).click()

    @allure.description('Клик на логотип «Самоката»')
    def click_logo_scooter(self):
        logo_scooter = self.wait_and_find_element(MainPageLocators.LOGO_SCOOTER)
        logo_scooter.click()

    @allure.description('Клик на логотип «Яндекс»')
    def click_logo_yandex(self):
        logo_yandex = self.wait_and_find_element(MainPageLocators.LOGO_YANDEX)
        logo_yandex.click()

    def open_question(self, question_locator):
        # Жмем на вопрос по переданному локатору
        question_element = self.wait_and_find_element(question_locator)
        # Прокручиваем к элементу
        self.driver.execute_script("arguments[0].scrollIntoView();", question_element)
        # Явно ждем, пока элемент станет кликабельным
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(question_element))
        question_element.click()

    def get_answer_text(self, answer_locator):
        try:
            # Явно ожидаем появления ответа
            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(answer_locator)
            )
            # Получаем элемент ответа по локатору
            answer_element = self.wait_and_find_element(answer_locator)
            return answer_element.text
        except TimeoutException:
            print("Ответ не появился в течение ожидаемого времени.")
            return ""



