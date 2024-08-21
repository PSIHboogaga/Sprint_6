from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_text_and_find_element(self, locator, text) -> WebElement:
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator)

    def open_page(self, url):
        self.driver.get(url)
