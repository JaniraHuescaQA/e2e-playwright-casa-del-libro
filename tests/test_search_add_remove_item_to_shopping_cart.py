from playwright.sync_api import Page, expect
import utils.utils as utils
from pages.home_page import HomePage
from pages.header_page import HeaderPage
from pages.results_page import ResultsPage
from pages.details_page import DetailsPage
from pages.shopping_cart_page import ShoppingCartPage

def test_search_add_remove_item_to_cart(page:Page):
    print("Given the user visits 'La Casa del Libro' homepage")
    home_page = HomePage(page)
    home_page.visit()

    print("And the user accepts the cookies")
    home_page.accept_cookies()

    print("When the user performs a search")
    header_page = HeaderPage(page)
    search_query = "harry potter"
    header_page.search(search_query)

    print("Then the user should see search results")
    resuls_page = ResultsPage(page)
    resuls_page.verify_results_message(search_query)
    resuls_page.verify_results_contain_search(search_query)

    print("When the user clicks on the desired result")
    product_name = "HARRY POTTER Y LA CAMARA SECRETA"
    resuls_page.click_on_result(product_name)

    print("And the user adds the item to the shopping cart")
    details_page = DetailsPage(page)
    details_page.add_to_cart()

    print("Then the shopping cart section should be visible")
    shopping_cart_page = ShoppingCartPage(page)
    shopping_cart_page.verify_cart_section_is_visible()

    print("And the user should see the added item in the cart")
    shopping_cart_page.verify_product_in_cart(product_name)

    print("When the user removes the item from the car")
    shopping_cart_page.remove_product_from_cart()

    print("Then the user should not see the item previously selected")
    shopping_cart_page.verify_product_not_in_cart()

    print("And the shopping cart should be empty")
    shopping_cart_page.verify_cart_is_empty()

    print("When the user closes the shopping cart section")
    shopping_cart_page.close_shopping_cart_section()

    print("Then the shopping cart section sholud not be visible")
    not shopping_cart_page.verify_cart_section_is_visible()