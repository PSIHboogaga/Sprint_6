import allure

from data import OrderData, Urls
from pages.order_page import OrderPage


class TestOrderSamokat:
    @allure.title('Проверка заказа самоката')
    @allure.description('Заполняем необходимые поля и оформляем заказ')
    def test_successful_ordering_a_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.MAIN_PAGE)
        order_page.click_order_button_up()
        order_page.set_name_field(OrderData.NAME)
        order_page.set_surname_field(OrderData.SURNAME)
        order_page.set_address_field(OrderData.ADRESS)
        order_page.set_phone_field(OrderData.PHONE)
        order_page.click_metro_button()
        order_page.select_metro_station()
        order_page.click_next_button()
        order_page.set_date(OrderData.DATE)
        order_page.click_rental_period()
        order_page.click_rental_period_sutki()
        order_page.click_submit_button()
        order_page.click_yes_button()

        expected_text = "Заказ оформлен"
        actual_text = order_page.find_actual_text()

        assert expected_text in actual_text
