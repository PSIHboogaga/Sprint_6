import pytest
import allure

from data import Urls, QuestionData
from locators.main_page_locator import QuestionLocators, AnswerLocators
from pages.main_page import MainPage

class TestQuestion:
    @allure.title('Проверка ответов на вопросы')
    @pytest.mark.parametrize(
        'question_locator, answer_locator, expected_answer',
        [
            (QuestionLocators.QUESTION_0, AnswerLocators.ANSWER_0, QuestionData.QUESTION_0_TEXT),
            (QuestionLocators.QUESTION_1, AnswerLocators.ANSWER_1, QuestionData.QUESTION_1_TEXT),
            (QuestionLocators.QUESTION_2, AnswerLocators.ANSWER_2, QuestionData.QUESTION_2_TEXT),
            (QuestionLocators.QUESTION_3, AnswerLocators.ANSWER_3, QuestionData.QUESTION_3_TEXT),
            (QuestionLocators.QUESTION_4, AnswerLocators.ANSWER_4, QuestionData.QUESTION_4_TEXT),
            (QuestionLocators.QUESTION_5, AnswerLocators.ANSWER_5, QuestionData.QUESTION_5_TEXT),
            (QuestionLocators.QUESTION_6, AnswerLocators.ANSWER_6, QuestionData.QUESTION_6_TEXT),
            (QuestionLocators.QUESTION_7, AnswerLocators.ANSWER_7, QuestionData.QUESTION_7_TEXT),
        ]
    )
    def test_question(self, driver, question_locator, answer_locator, expected_answer):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)  # Переходим на главную страницу
        main_page.open_question(question_locator)  # Открываем соответствующий вопрос
        actual_answer = main_page.get_answer_text(answer_locator)  # Получаем текст ответа
        assert actual_answer == expected_answer, f'нужный ответ: {expected_answer}, полученный ответ: {actual_answer}' # Ассертим, что текст ответа соответствует ожидаемому