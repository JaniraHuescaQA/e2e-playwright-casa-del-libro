from playwright.sync_api import Page, expect
import re

class MyAccountPage:
    def __init__(self, page: Page):
        """ 
        Constructor to initialize the MyAccountPage class with the Playwright Page object.
        This allows us to interact with the webpage. 
        """
        self.page = page

    def go_to_signup(self):
        """ Clicks on the 'Registrarme' link to navigate to the signup page """
        self.page.wait_for_timeout(1000) # Small delay to ensure UI stability
        self.page.get_by_role("link", name="Registrarme").click()
        expect(self.page).to_have_url(re.compile(".*register-access.*"))

    def go_to_login(self):
        """ Clicks on the 'Iniciar Sesión' link to navigate to the login page """
        self.page.wait_for_timeout(1000) # Small delay to ensure UI stability
        self.page.locator("a#b-i-s-c").click()
        expect(self.page).to_have_url(re.compile(".*login-access.*"))