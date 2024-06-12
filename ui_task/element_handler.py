import random
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from ui_task_test_data import timeout_default


class ElementHandler:
    def __init__(self, driver):
        self.driver = driver

    def element_handler_click_actual_element(self, element_locator, element_name):
        element = WebDriverWait(self.driver, timeout_default).until(ec.element_to_be_clickable(element_locator), f"Execution stopped: {element_name} cannot be clicked.")
        element.click()

    def element_handler_click_random_element(self, element_locator, element_name):
        elements = WebDriverWait(self.driver, timeout_default).until(ec.visibility_of_all_elements_located(element_locator), f"Execution stopped: {element_name} cannot be clicked.")
        random_element = random.choice(elements)
        random_element.click()

    def element_handler_get_element_text(self, element_locator, element_name):
        element = WebDriverWait(self.driver, timeout_default).until(ec.visibility_of_element_located(element_locator), f"Execution stopped: {element_name} cannot be obtained.")
        element_text = element.text
        return element_text

    def element_handler_get_current_url(self):
        current_url = self.driver.current_url
        return current_url
