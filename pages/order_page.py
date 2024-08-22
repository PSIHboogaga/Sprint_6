import allure

from locators.main_page_locator import MainPageLocators
from locators.order_page_locator import OrderPageLocators
from pages.base_page import BasePage



class OrderPage(BasePage):
    @allure.step("Клик кнопки заказать(вверху)")
    def click_order_button_up(self):
        self.wait_and_find_element(*MainPageLocators.BUTTON_ORDER_UP).click()
    @allure.step('Заполняем поле имя')
    def set_name_field(self, name):
        self.wait_and_find_element(*OrderPageLocators.NAME_INPUT).send_keys(name)
    @allure.step('Заполняем поле фамилия')
    def set_surname_field(self, surname):
        self.wait_and_find_element(*OrderPageLocators.SURNAME_INPUT).send_keys(surname)

    @allure.step('Заполняем поле фамилия')
    def set_adress_field(self, adress):
        self.wait_and_find_element(*OrderPageLocators.ADRESS_INPUT).send_keys(adress)

    @allure.step('Заполняем поле телефон')
    def set_phone_field(self, phone):
        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone)
    @allure.step('Нажимаем на поле метро')
    def click_metro_button(self):
        self.wait_and_find_element(*OrderPageLocators.METRO_INPUT).click()

    @allure.step('Вводим Черкизовская')
    def select_metro(self, metro):
        self.wait_and_find_element(*OrderPageLocators.METRO_INPUT).send_keys(metro)

    @allure.step('Нажимаем кнопку далее')
    def click_next_button(self):
        self.wait_and_find_element(*OrderPageLocators.BUTTON_NEXT).click()

    @allure.step('Нажимаем на поле когда привезти самокат')
    def click_time_field(self):
        self.wait_and_find_element(*OrderPageLocators.TIME_FIELD).click()

    @allure.step('Выбираем дату')
    def click_time_field_select(self):
        self.wait_and_find_element(*OrderPageLocators.TIME_FIELD_SELECT).click()

    @allure.step('Выбираем период')
    def click_rental_period(self):
        self.wait_and_find_element(*OrderPageLocators.RENTAL_PERIOD).click()
        self.wait_and_find_element(*OrderPageLocators.RENTAL_PERIOD_SELECT).click()

    @allure.step('Нажимаем кнопку заказать')
    def click_submit_button(self):
        self.wait_and_find_element(*OrderPageLocators.SUBMIT_BUTTON).click()

    @allure.step('Нажимаем кнопку да')
    def click_yes_button(self):
        self.wait_and_find_element(*OrderPageLocators.BUTTON_YES).click()

    def order(self, name, surname, adress, phone, metro):
        self.click_order_button_up()
        self.set_name_field(name)
        self.set_surname_field(surname)
        self.set_adress_field(adress)
        self.set_phone_field(phone)
        self.click_metro_button()
        self.select_metro(metro)
        self.click_next_button()
        self.click_time_field()
        self.click_time_field_select()
        self.click_rental_period()
        self.click_submit_button()
        self.click_yes_button()



