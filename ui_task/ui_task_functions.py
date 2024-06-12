from selenium import webdriver
from ui_task_test_data import max_redirects_limit, target_article_title


def initialize_driver(starting_url):
    driver = webdriver.Chrome()
    driver.get(starting_url)
    driver.maximize_window()
    return driver


def get_article_title_and_url(wiki_article_page):
    article_title = wiki_article_page.get_article_title()
    article_url = wiki_article_page.get_article_url()
    article_title_and_url = (article_title, article_url)
    return article_title, article_url, article_title_and_url


def check_max_redirects_limit(redirects_number):
    if redirects_number == max_redirects_limit:
        max_redirects_limit_reached = True
    else:
        max_redirects_limit_reached = False
    return max_redirects_limit_reached


def add_article_title_and_url_to_list(visited_articles_title_and_url, article_title_and_url):
    visited_articles_title_and_url.append(article_title_and_url)
    return visited_articles_title_and_url


def check_loop_occurred(article_title_and_url, visited_articles_title_and_url):
    if article_title_and_url in visited_articles_title_and_url:
        loop_occurred = True
    else:
        loop_occurred = False
    return loop_occurred


def print_result(max_redirects_limit_reached, loop_occurred, article_title, article_url, redirects_number, visited_articles_title_and_url):
    if max_redirects_limit_reached:
        print(f"\nExecution stopped: Maximum number of redirects ({max_redirects_limit}) performed before reaching '{target_article_title}' article.")
    elif loop_occurred:
        print(f"\nExecution stopped: Loop occurred, article: '{article_title}' with URL: '{article_url}' was visited twice. Number of redirects: {redirects_number}")
    else:
        print(f"\nSuccess, article '{target_article_title}' reached. Number of redirects: {redirects_number}.")
    print("\nVisited articles:", *visited_articles_title_and_url, sep="\n")


def quit_driver(driver):
    driver.quit()
