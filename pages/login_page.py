from playwright.sync_api import Page, expect
import utils.utils as utils

class LoginPage:
    def __init__(self, page: Page):
        """ 
        Constructor to initialize the LoginPage class with the Playwright Page object.
        This allows us to interact with the webpage. 
        """
        self.page = page    

    def disable_hover_for_modals(self):
        """ 
        Disables hover interactions and hides the floating menu modal that appears when the user hovers over certain elements. 
        This prevents unwanted modals from appearing and potentially blocking important UI elements during automated tests. 
        """
        self.page.add_style_tag(content="""
        .floating-menu {
            display: none !important;
        }
        """)

    def fill_email(self, email: str):
        """ Clears and fills the email field """
        self.page.get_by_label("Email*").clear()
        self.page.get_by_label("Email*").fill(email)

    def fill_password(self, password: str):
        """ Clears and fills the password field """
        self.page.get_by_label("Contraseña*").clear()
        self.page.get_by_label("Contraseña*").fill(password)

    def click_login_button(self):
        """ Clicks on the login button """
        self.page.get_by_role("button", name="iniciar sesión").click(force=True)
    
    def verify_login(self):
        expect(self.page.locator('img[src="/img/cabecera/ico_usuario_check.svg"]')).to_be_visible()
        if not utils.is_mobile(self.page):
            expect(self.page.locator("#b-u-l")).to_contain_text("Janira")
        
    def get_error_message(self, message: str):
        """ Checks if a specific error message is visible """
        return expect(self.page.get_by_text(message, exact=True)).to_be_visible()