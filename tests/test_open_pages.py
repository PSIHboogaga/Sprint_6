import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls
from locators.main_page_locator import MainPageLocators
from pages.main_page import MainPage


class TestOpenPageScooter:
    @allure.title('Проверка открытия страниц по клику')
    @allure.description('Кликаем на логотип «Самокат»')
    def test_open_page_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(*MainPageLocators.LOGO_SCOOTER))
        main_page.click_logo_scooter()

        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/', (
            'Страница яндекс самокат не открыта')  # Проверяем, что перешли на главную страницу «Самоката»



class TestOpenPageDzen:
    @allure.description('Кликаем на логотип «Яндекс»')
    def test_open_page_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(*MainPageLocators.LOGO_YANDEX))
        main_page.click_logo_yandex()

        assert driver.current_url == 'https://dzen.ru/?yredirect=true', (
            'Страница ДЗЕН не открыта')  # Проверяем, что перешли на Dzen

