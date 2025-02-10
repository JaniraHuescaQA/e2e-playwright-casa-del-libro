from playwright.sync_api import Page, expect
import utils.utils as utils

class ResultsPage:
    def __init__(self, page: Page):
        """ 
        Constructor to initialize the ResultsPage class with the Playwright Page object.
        This allows us to interact with the webpage. 
        """
        self.page = page

    def verify_no_results_message(self):
        """ Checks if the 'no results' message is displayed """
        no_results_message = self.page.locator("[data-test=\"no-results-message\"]")
        expect(no_results_message).to_be_visible()
        expect(no_results_message).to_contain_text("No se han encontrado resultados para ")

    def verify_results_message(self, search_query: str):
        """ Checks that the page displays the number of search results """
        if not (utils.is_mobile(self.page)):
            expect(self.page.get_by_text(f"resultados para {search_query}")).to_be_visible()

    def verify_results_contain_search(self, search_query: str):
        """ Checks that the results contain the searched term """
        # Verify that the results shown are related to the search performed
        expect(self.page.locator("[data-test=\"base-grid\"]")).to_contain_text(search_query)
    
    def click_on_result(self, product_name: str):
        """ Clicks on a product in the results list """
        product_locator = self.page.locator(f"[data-test='result-title']", has_text=product_name)
        product_locator.first.click()