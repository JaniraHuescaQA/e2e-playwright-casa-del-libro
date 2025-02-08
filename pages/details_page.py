from playwright.sync_api import Page, expect
import utils.utils as utils

class DetailsPage:
    def __init__(self, page: Page):
        """ 
        Constructor to initialize the DetailsPage class with the Playwright Page object.
        This allows us to interact with the webpage. 
        """
        self.page = page

    def add_to_cart(self):
        """ Clicks on the 'Add to cart' button """
        self.page.get_by_role("button", name="Añadir a la cesta").first.click()