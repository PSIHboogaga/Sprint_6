import allure
import pytest

from data import OrderData, Urls
from locators.order_page_locator import OrderPageLocators
from pages.order_page import OrderPage


@pytest.fixture
def buttone_locator():
    return OrderPageLocators.BUTTON_ORDER_DOWN


class TestOrderSamokats:
    @allure.title('Проверка заказа самоката через нижнюю кнопку')
    @allure.description('Заполняем необходимые поля и оформляем заказ')
    def test_successful_ordering_a_scooter_down(self, driver, buttone_locator):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.MAIN_PAGE)
        order_page.click_order_button_down(buttone_locator)
        order_page.set_name_field(OrderData.NAME_)
        order_page.set_surname_field(OrderData.SURNAME_)
        order_page.set_address_field(OrderData.ADRESS_)
        order_page.set_phone_field(OrderData.PHONE_)
        order_page.click_metro_button()
        order_page.select_metro_station()
        order_page.click_next_button()
        order_page.set_date(OrderData.DATE_)
        order_page.click_rental_period()
        order_page.click_rental_period_sutki()
        order_page.click_submit_button()
        order_page.click_yes_button()

        expected_text = "Заказ оформлен"
        actual_text = order_page.find_actual_text()

        assert expected_text in actual_text
