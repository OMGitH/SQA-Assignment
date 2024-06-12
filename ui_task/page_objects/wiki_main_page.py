from selenium.webdriver.common.by import By
from element_handler import ElementHandler


class WikiMainPage(ElementHandler):

    # Identification of elements.
    article_link_on_this_day = {
        "locator": (By.XPATH, "//div[@id='mp-otd']//a[starts-with(@href, '/wiki/')][not(parent::span[contains(@typeof, 'File')])]"),
        "name": "Link in 'On this day' section"
    }

    # Actions
    def open_random_article(self):
        self.element_handler_click_random_element(self.article_link_on_this_day["locator"], self.article_link_on_this_day["name"])
