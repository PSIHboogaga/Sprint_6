import allure

from data import Urls
from locators.main_page_locator import MainPageLocators
from pages.main_page import MainPage


class TestOpenPageScooter:
    @allure.title('Проверка открытия страниц по клику')
    @allure.description('Кликаем на логотип «Самокат»')
    def test_open_page_dzen(self, driver):
        main_page = MainPage(driver)
        #main_page.open_page(Urls.MAIN_PAGE)

        main_page.click_logo_scooter()

        assert main_page.get_current_banner(*MainPageLocators.LOGO_SCOOTER) == 'https://qa-scooter.praktikum-services.ru', (
            'Страница яндекс самокат не открыта')


class TestOpenPageYandex:
    @allure.description('Кликаем на логотип «Яндекс»')
    def test_open_page_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)

        main_page.click_logo_yandex()

        assert main_page.get_current_banner(*MainPageLocators.LOGO_YANDEX) == 'https://dzen.ru/?yredirect=true', (
            'Страница ДЗЕН не открыта')