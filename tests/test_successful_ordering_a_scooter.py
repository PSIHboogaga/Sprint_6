import allure

from data import OrderData, Urls, TheOrderHasBeenPlaced
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
        order_page.set_adress_field(OrderData.ADRESS)
        order_page.set_phone_field(OrderData.PHONE)
        order_page.click_metro_button()
        order_page.select_metro(OrderData.METRO)
        order_page.click_next_button()
        order_page.click_time_field()
        order_page.click_time_field_select()
        order_page.click_rental_period()
        order_page.click_submit_button()
        order_page.click_yes_button()




        order_page = OrderPage(driver)

        assert order_page.get_current_banner(TheOrderHasBeenPlaced.ORDEROK) == TheOrderHasBeenPlaced.ORDEROK, ('Заказ не оформлен')