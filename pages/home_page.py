from playwright.sync_api import Page

class HomePage:
    URL = "https://www.casadellibro.com"

    def __init__(self, page: Page):
        """ 
        Constructor to initialize the HomePage class with the Playwright Page object.
        This allows us to interact with the webpage. 
        """
        self.page = page

    def visit(self):
        """
        Navigates to the homepage of 'Casa del Libro'
        """
        self.page.goto(self.URL)

    def accept_cookies(self):
        """
        Waits for the cookie banner to appear and accepts cookies by clicking the button
        """
        self.page.wait_for_selector("button:has-text('Aceptar')")
        self.page.get_by_role("button", name="Aceptar").click()