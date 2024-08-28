import allure

from locators.order_page_locator import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Клик кнопки заказать (вверху)")
    def click_order_button_up(self):
        order_button_up = self.wait_and_find_element(OrderPageLocators.BUTTON_ORDER_UP)
        order_button_up.click()

    @allure.step("Заполняем поле имя")
    def set_name_field(self, name):
        name_field = self.wait_and_find_element(OrderPageLocators.NAME_INPUT)
        name_field.send_keys(name)

    @allure.step("Заполняем поле фамилия")
    def set_surname_field(self, surname):
        surname_field = self.wait_and_find_element(OrderPageLocators.SURNAME_INPUT)
        surname_field.send_keys(surname)

    @allure.step("Заполняем поле адрес")
    def set_address_field(self, address):
        address_field = self.wait_and_find_element(OrderPageLocators.ADRESS_INPUT)
        address_field.send_keys(address)

    @allure.step("Заполняем поле телефон")
    def set_phone_field(self, phone):
        phone_field = self.wait_and_find_element(OrderPageLocators.PHONE_INPUT)
        phone_field.send_keys(phone)

    @allure.step("Нажимаем на поле метро")
    def click_metro_button(self):
        metro_button = self.wait_and_find_element(OrderPageLocators.METRO_INPUT)
        metro_button.click()

    # @allure.step("Клик на метро")
    # def select_metro(self, metro):
    #     metro_field = self.wait_and_find_element(OrderPageLocators.METRO_INPUT)
    #     metro_field.send_keys(metro)

    @allure.step("Выбираем метро")
    def select_metro_station(self):
        metro_station = self.wait_and_find_element(OrderPageLocators.METRO_CHERK)
        metro_station.click()

    @allure.step("Нажимаем кнопку далее")
    def click_next_button(self):
        next_button = self.wait_and_find_element(OrderPageLocators.BUTTON_NEXT)
        next_button.click()

    @allure.step("Вводим дату")
    def set_date(self, date):
        time_field = self.wait_and_find_element(OrderPageLocators.TIME_FIELD)
        time_field.send_keys(date)

    @allure.step("Выбираем период аренды")
    def click_rental_period(self):
        rental_period = self.wait_and_find_element(OrderPageLocators.RENTAL_PERIOD)
        rental_period.click()

    @allure.step("Выбираем сутки")
    def click_rental_period_sutki(self):
        rental_period_sutki = self.wait_and_find_element(OrderPageLocators.RENTAL_PERIOD_SELECT)
        rental_period_sutki.click()

    @allure.step("Нажимаем кнопку заказать")
    def click_submit_button(self):
        submit_button = self.wait_and_find_element(OrderPageLocators.SUBMIT_BUTTON)
        submit_button.click()

    @allure.step("Нажимаем кнопку да на подтверждение")
    def click_yes_button(self):
        yes_button = self.wait_and_find_element(OrderPageLocators.BUTTON_YES)
        yes_button.click()




    # @allure.step("Оформляем заказ")
    # def order(self, name, surname, address, phone, metro):
    #     self.click_order_button_up()
    #     self.set_name_field(name)
    #     self.set_surname_field(surname)
    #     self.set_address_field(address)
    #     self.set_phone_field(phone)
    #     self.click_metro_button()
    #     self.select_metro(metro)
    #     self.click_next_button()
    #     self.click_time_field()
    #     self.click_time_field_select()
    #     self.click_rental_period()
    #     self.click_submit_button()
    #     self.click_yes_button()


