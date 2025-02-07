from playwright.sync_api import Page, expect

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
