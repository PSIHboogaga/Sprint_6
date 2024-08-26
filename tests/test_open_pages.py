import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls
from pages.main_page import MainPage

class TestOpenPageScooter:
    @allure.title('Проверка открытия страниц по клику')
    @allure.description('Кликаем на логотип «Самокат»')
    def test_open_page_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_logo_scooter()

        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/', (
            'Страница яндекс самокат не открыта')  # Проверяем, что перешли на главную страницу «Самоката»



class TestOpenPageDzen:
    @allure.description('Кликаем на логотип «Яндекс»')
    def test_open_page_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_logo_yandex()
        WebDriverWait(driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(expected_conditions.url_contains('https://dzen.ru/'))

        assert driver.current_url == 'https://dzen.ru/?yredirect=true', (
            'Страница ДЗЕН не открыта')  # Проверяем, что перешли на Dzen

