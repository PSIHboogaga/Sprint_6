import pytest
import allure

from data import QuestionsAboutImportantThingsData
from pages.main_page import MainPage


class TestQuestion:
    @allure.title('Проверка ответов на вопросы')
    @pytest.mark.parametrize(QuestionsAboutImportantThingsData.param, QuestionsAboutImportantThingsData.value)
    def test_question(self, driver, question, expected_answer):
        main_page = MainPage(driver)

        questions = main_page.driver.find_elements(*MainPage.open_faq) # Найти и открыть вопрос

        for index, element in enumerate(questions):    # Ищем вопрос по тексту
            if element.text == question:
                element.click()  # Кликаем по вопросу
                break

        actual_answer = main_page.get_faq_answer(index)  # Получаем ответ на вопрос

        assert actual_answer == expected_answer   # Проверяем, что полученный ответ совпадает с ожидаемым




