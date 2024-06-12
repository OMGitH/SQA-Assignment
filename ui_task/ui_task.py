from page_objects.wiki_article_page import WikiArticlePage
from page_objects.wiki_main_page import WikiMainPage
from ui_task_functions import initialize_driver, check_max_redirects_limit, quit_driver, print_result, get_article_title_and_url, add_article_title_and_url_to_list, check_loop_occurred
from ui_task_test_data import target_article_title, wiki_main_page_url

redirects_number = 0
max_redirects_limit_reached = False
loop_occurred = False
visited_articles_title_and_url = []


driver = initialize_driver(wiki_main_page_url)

wiki_main_page = WikiMainPage(driver)
wiki_article_page = WikiArticlePage(driver)

# Open random article from Wikipedia main page section On this day.
wiki_main_page.open_random_article()
article_title, article_url, article_title_and_url = get_article_title_and_url(wiki_article_page)
visited_articles_title_and_url = add_article_title_and_url_to_list(visited_articles_title_and_url, article_title_and_url)

# Getting to article about Philosophy.
while article_title != target_article_title:

    # Check if redirects limit is reached.
    if check_max_redirects_limit(redirects_number):
        max_redirects_limit_reached = True
        break

    redirects_number = wiki_article_page.click_first_valid_link(driver, redirects_number, article_title, article_url, visited_articles_title_and_url)
    article_title, article_url, article_title_and_url = get_article_title_and_url(wiki_article_page)

    # Check if loop occurs.
    loop_occurred = check_loop_occurred(article_title_and_url, visited_articles_title_and_url)

    visited_articles_title_and_url = add_article_title_and_url_to_list(visited_articles_title_and_url, article_title_and_url)

    if loop_occurred:
        break

print_result(max_redirects_limit_reached, loop_occurred, article_title, article_url, redirects_number, visited_articles_title_and_url)

quit_driver(driver)
