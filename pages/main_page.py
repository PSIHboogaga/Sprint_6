import allure

from locators.main_page_locator import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.description('Клик кнопки заказать(вверху\внизу)')
    def click_order_button(self, index):
        order_button = MainPageLocators.BUTTON_ORDER_UP if index == 0 else MainPageLocators.BUTTON_ORDER_DOWN
        self.wait_and_find_element(order_button).click()

    @allure.description('Клик на логотип «Самоката»')
    def click_logo_scooter(self):
        self.driver.find_element(*MainPageLocators.LOGO_SCOOTER).click()
    @allure.description('Клик на логотип «Яндекс»')
    def click_logo_yandex(self):
        self.driver.find_element(*MainPageLocators.LOGO_YANDEX).click()

    def open_faq(self, index):
        faq_buttons = self.driver.find_elements(*MainPageLocators.FAQ_BUTTONS)
        faq_buttons[index].click()

    def get_faq_answer(self, index):
        faq_answers = self.driver.find_elements(*MainPageLocators.FAQ_ANSWERS)
        return faq_answers[index].text






