import allure

from locators.main_page_locator import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Клик на логотип «Самоката»')
    def click_logo_scooter(self):
        logo_scooter = self.wait_and_find_element(MainPageLocators.LOGO_SCOOTER)
        logo_scooter.click()

    @allure.step('Клик на логотип «Яндекс»')
    def click_logo_yandex(self):
        logo_yandex = self.wait_and_find_element(MainPageLocators.LOGO_YANDEX)
        logo_yandex.click()

    @allure.step('Клик на вопрос')
    def open_question(self, question_locator):

        question_element = self.wait_and_find_element(question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", question_element)  # Прокручиваем к элементу
        self.wait_and_find_element(question_locator)
        question_element.click()

    @allure.step('получаем ответ')
    def get_answer_text(self, answer_locator):
        self.wait_for_element_to_appear(answer_locator)  # Ожидаем появления ответа
        answer_element = self.wait_and_find_element(answer_locator)  # Получаем элемент ответа по локатору
        return answer_element.text
