from playwright.sync_api import Page, expect
import re
import utils.utils as utils

class MenuPage:
    def __init__(self, page: Page):
        """ 
        Constructor to initialize the MenuPage class with the Playwright Page object.
        This allows us to interact with the webpage. 
        """
        self.page = page

    def open_menu(self):
        """ Opens the navigation menu if the viewport is mobile-sized. """
        if utils.is_mobile(self.page):
            # Small delay to ensure UI stability
            self.page.wait_for_timeout(1000)
            # Locate the element menu by locator, and click on it
            self.page.locator("button[name='menu']").click()

    def click_menu_link(self, category_name: str, subcategory_name: str = None):
        """ 
        Clicks on a menu link, considering mobile and desktop versions.
        Args:
            category_name (str): The main category name to click.
            subcategory_name (str, optional): The subcategory name if needed. 
        """
        if utils.is_mobile(self.page):
            self.open_menu()
            if category_name == "Ofertas":
                self.page.get_by_role("link", name=category_name, exact=True).click()
            else:
                # Locate the element by role (button) and for exact text, and click on it
                if category_name == "eBooks":
                    self.page.get_by_role("button", name=category_name, exact=True).first.click()
                else:
                    self.page.get_by_role("button", name=category_name, exact=True).click()
                if subcategory_name:
                    # Locate the element by role (link), and click on it
                    self.page.get_by_role("link", name=subcategory_name).click()
        else:
            # Small delay to ensure UI stability
            self.page.wait_for_timeout(1000)
            # Locate the element by role (link) and for exact text, and click on it
            if category_name == "Ficción" or category_name == "Infantil" or category_name == "Juvenil" or category_name == "English books" or category_name == "Llibres en català" or category_name == "Papelería":
                self.page.get_by_role("link", name=category_name, exact=True).first.click()
            elif category_name == "eBooks":
                self.page.get_by_role("link", name="eBooks", exact=True).nth(2).click()
            else:
                self.page.get_by_role("link", name=category_name, exact=True).click()

    def verify_page(self, expected_url_keyword: str, expected_title: str, heading_text: str):
        """ 
        Verifies that the user is on the correct page after clicking a menu link.
        Args:
            expected_url_keyword (str): A keyword to check in the URL.
            expected_title (str): The expected title of the page.
            heading_text (str): The expected heading text on the page.
        """
        # Check that URL page contains the word {expected_url_keyword}
        expect(self.page).to_have_url(re.compile(expected_url_keyword))
        # Check that title page has the exact text {expected_title}
        expect(self.page).to_have_title(expected_title)
        # Locate the element of type 'heading' and filter by {heading_text}, and check that is visibe
        expect(self.page.get_by_role("heading", name=heading_text, exact=True)).to_be_visible()