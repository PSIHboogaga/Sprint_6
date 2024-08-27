# import allure
#
# from data import OrderData, Urls, TheOrderHasBeenPlaced
# from pages.order_page import OrderPage
#
#
#
# class TestOrderSamokat:
#
#     @allure.title('Проверка заказа самоката')
#     @allure.description('Заполняем необходимые поля и оформляем заказ')
#     def test_successful_ordering_a_scooter(self, driver):
#         order_page = OrderPage(driver)
#         order_page.open_page(Urls.MAIN_PAGE)
#
#         order_page.click_order_button_up()
#         order_page.set_name_field(OrderData.NAME)
#         order_page.set_surname_field(OrderData.SURNAME)
#         order_page.set_adress_field(OrderData.ADRESS)
#         order_page.set_phone_field(OrderData.PHONE)
#         order_page.click_metro_button()
#         order_page.select_metro(OrderData.METRO)
#         order_page.click_next_button()
#         order_page.click_time_field()
#         order_page.click_time_field_select()
#         order_page.click_rental_period()
#         order_page.click_submit_button()
#         order_page.click_yes_button()
#
#
#
#
#         order_page = OrderPage(driver)
#
#         assert order_page.get_current_banner(TheOrderHasBeenPlaced.ORDEROK) == TheOrderHasBeenPlaced.ORDEROK, ('Заказ не оформлен')
#
#         # def get_success_message(self):
#         # return self.wait_and_find_element(OrderPageLocators.SUCCESS_MESSAGE).text


import pytest
import allure
from data import QuestionData  # Импортируйте ваши данные для теста
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import Urls


@allure.title('Тест на заказ самоката: позитивный сценарий')
@pytest.mark.parametrize("name, surname, address, phone, metro", [
    ("Иван", "Иванов", "Улица 1", "+79000000000", "Черкизовская"),
    ("Петр", "Петров", "Улица 2", "+79000000001", "Таганская"),
])
def test_order_scooter(driver, name, surname, address, phone, metro):
    main_page = MainPage(driver)
    main_page.open_page(Urls.MAIN_PAGE)

    main_page.click_order_button()  # Кнопка «Заказать» вверху страницы click
    order_page = OrderPage(driver)

    # Заполняем форму заказа
    order_page.order(name, surname, address, phone, metro)

    # Проверяем успешное создание заказа (всплывающее окно)
    assert order_page.is_order_successful(), "Ожидалось успешное создание заказа."

    # Возвращаемся на главную страницу для второго входа
    main_page.open_page(Urls.MAIN_PAGE)

    # Точка входа 2: Кнопка «Заказать» внизу страницы
    main_page.click_order_button_down()
    order_page.order(name, surname, address, phone, metro)

    # Проверяем успешное создание заказа (всплывающее окно)
    assert order_page.is_order_successful(), "Ожидалось успешное создание заказа."



@allure.step('Проверка успешного создания заказа')
def is_order_successful(self):
    try:
        # Явно ожидаем появления сообщения об успешном создании заказа
        success_message = self.wait_and_find_element(OrderPageLocators.SUCCESS_MESSAGE)  # Предположим, что у вас есть локатор для сообщения об успехе
        return success_message.is_displayed()  # Возвращает True, если сообщение отображается
    except TimeoutException:
        return False