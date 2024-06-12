from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from element_handler import ElementHandler
from ui_task_functions import quit_driver


class WikiArticlePage(ElementHandler):

    # Identification of elements.
    # First link in main body of article that points to Wikipedia article, so it is not external and does not point to non-existent page.
    first_article_link_valid = {
        "locator": (By.XPATH, "(//div[contains(@class, 'mw-content-ltr')]/p//a[starts-with(@href, '/wiki/')])[1]"),
        "name": "Valid link"
    }
    article_title = {
        "locator": (By.CSS_SELECTOR, "h1#firstHeading"),
        "name": "Article title"
    }

    # Actions
    def click_first_valid_link(self, driver, redirects_number, article_title, article_url, visited_articles_title_and_url):
        try:
            self.element_handler_click_actual_element(self.first_article_link_valid["locator"], self.first_article_link_valid["name"])
            redirects_number += 1
        except TimeoutException as exception:
            print(f"\nExecution stopped: Cannot continue from article: '{article_title}' with URL: '{article_url}', probably there is no valid link.")
            print("\nVisited articles:", *visited_articles_title_and_url, "\n", sep="\n")
            quit_driver(driver)
            raise exception
        return redirects_number

    def get_article_title(self):
        article_title = self.element_handler_get_element_text(self.article_title["locator"], self.article_title["name"])
        article_title = article_title.strip()
        return article_title

    def get_article_url(self):
        article_url = self.element_handler_get_current_url()
        return article_url
