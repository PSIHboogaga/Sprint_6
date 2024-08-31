from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)
    
    def wait_text_and_find_element(self, locator, text) -> WebElement:
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator)

    def wait_for_element_to_appear(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def open_page(self, url):
        self.driver.get(url)

    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_dzen_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains('https://dzen.ru/'))

    def scroll_to_element(self, element):
       self.driver.execute_script("arguments[0].scrollIntoView();", element)  # Прокручиваем к элементу
