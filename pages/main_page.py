import allure

from locators.main_page_locator import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
@allure.step('Клик кнопки заказать(вверху)')
def click_order_button_top(self):
    self.driver.find_element(MainPageLocators.ORDER_BUTTON_TOP).click()
@allure.step('Клик кнопки заказать(внизу)')

def click_order_button_bottom(self):
    self.driver.find_element(MainPageLocators.ORDER_BUTTON_BOTTOM).click()

@allure.step('Клик на логотип «Самоката»')
def click_logo_scooter(self):
    self.driver.find_element(MainPageLocators.LOGO_SCOOTER).click()

@allure.step('Клик на логотип «Яндекс»')
def click_logo_yandex(self):
    self.driver.find_element(MainPageLocators.LOGO_YANDEX).click()

