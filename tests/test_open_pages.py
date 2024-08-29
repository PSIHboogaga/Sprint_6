import allure

from data import Urls
from pages.main_page import MainPage

class TestOpenPageScooter:
    @allure.title('Проверка открытия страниц по клику')
    @allure.description('Кликаем на логотип «Самокат»')
    def test_open_page_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_logo_scooter()
        main_page.wait_for_time()
        assert main_page.get_current_url() == Urls.MAIN_PAGE, ('Страница самоката не открыта')

class TestOpenPageDzen:
    @allure.description('Кликаем на логотип «Яндекс»')
    def test_open_page_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_logo_yandex()
        main_page.switch_to_new_window()
        main_page.wait_for_dzen_page()

        assert main_page.get_current_url() == Urls.DZEN_PAGE, (
            'Страница ДЗЕН не открыта')  # Проверяем, что перешли на Dzen