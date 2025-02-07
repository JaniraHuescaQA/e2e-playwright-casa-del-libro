from pages.home_page import HomePage
from pages.header_page import HeaderPage
from pages.results_page import ResultsPage
import utils.utils as utils

def test_invalid_search(page):
    print("Given the user visits 'La Casa del Libro' homepage")
    home_page = HomePage(page)
    home_page.visit()

    print("And the user accepts the cookies")
    home_page.accept_cookies()

    print("When the user performs an invalid search")
    header_page = HeaderPage(page)
    header_page.search("..")  # Invalid search

    print("Then the user should see a message indicating that no results were found")
    results_page = ResultsPage(page)
    results_page.verify_no_results_message()