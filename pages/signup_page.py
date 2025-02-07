from playwright.sync_api import Page, expect

class SignupPage:
    def __init__(self, page: Page):
        """ 
        Constructor to initialize the SignupPage class with the Playwright Page object.
        This allows us to interact with the webpage. 
        """
        self.page = page    

    def fill_first_name(self, name: str):
        """ Clears and fills the first name field """
        self.page.get_by_label("Nombre*").clear()
        self.page.get_by_label("Nombre*").fill(name)

    def fill_last_name(self, surname: str):
        """ Clears and fills the last name field """
        self.page.get_by_label("Apellidos*").clear()
        self.page.get_by_label("Apellidos*").fill(surname)

    def fill_email(self, email: str):
        """ Clears and fills the email field """
        self.page.get_by_label("Email*").clear()
        self.page.get_by_label("Email*").fill(email)

    def fill_password(self, password: str):
        """ Clears and fills the password field """
        self.page.get_by_label("Contraseña*").clear()
        self.page.get_by_label("Contraseña*").fill(password)

    def click_register_button(self):
        """ Clicks on the register button """
        self.page.get_by_role("button", name="Registrarme").click()

    def get_error_message(self, message: str):
        """ Checks if a specific error message is visible """
        return expect(self.page.get_by_text(message, exact=True)).to_be_visible()