import pytest

from data import Questions_About_Important_Things_Data
from locators.main_page_locator import MainPageLocators
from pages.main_page import MainPage


class TestQuestion:

    @pytest.mark.parametrize(Questions_About_Important_Things_Data.param, Questions_About_Important_Things_Data.value)
    def test_question(self, driver, number, expected_answer):

        print(MainPageLocators.get_question_answer(number))

        main_page = MainPage(driver)

        element = main_page.wait_and_find_element()

        assert element.text == expected_answer
