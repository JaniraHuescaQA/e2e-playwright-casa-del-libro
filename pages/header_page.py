from playwright.sync_api import Page, expect
import re
import utils.utils as utils

class HeaderPage:
    def __init__(self, page: Page):
        """ 
        Constructor to initialize the HeaderPage class with the Playwright Page object.
        This allows us to interact with the webpage. 
        """
        self.page = page

    def open_menu(self):
        """ Opens the navigation menu if the viewport is mobile-sized. """
        self.page.wait_for_timeout(500) # Small delay to ensure UI stability
        self.page.locator("button[name='menu']").click()

    def click_category_mobile(self, category_name: str):
        """Clicks the category in mobile version (special logic for 'Ofertas')."""
        if category_name == "Ofertas":
            self.page.get_by_role("link", name=category_name, exact=True).click()
        else:
            self.page.get_by_role("button", name=category_name, exact=True).first.click()

    def click_category_desktop(self, category_name: str):
        """Clicks the category in desktop version (handles 'eBooks' separately)."""
        self.page.wait_for_timeout(1000) # Small delay for UI stability
        if category_name == "eBooks":
            self.page.get_by_role("link", name=category_name, exact=True).nth(2).click()
        else:
            self.page.get_by_role("link", name=category_name, exact=True).first.click()
    
    def click_subcategory(self, subcategory_name: str):
        """Clicks on the subcategory if provided."""
        if subcategory_name:
            self.page.get_by_role("link", name=subcategory_name).click()

    def click_menu_link(self, category_name: str, subcategory_name: str = None):
        """
        Handles menu clicks for both categories and subcategories (mobile/desktop).
        Args:
            category_name (str): The main category name to click.
            subcategory_name (str, optional): The subcategory name if needed.
        """
        if utils.is_mobile(self.page):
            self.open_menu()
            self.click_category_mobile(category_name)
            if subcategory_name:
                self.click_subcategory(subcategory_name)
        else:
            self.click_category_desktop(category_name)

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

    def go_to_my_account(self):
        """ Clicks on the account button to open the My Account menu """
        self.page.locator("#b-u-nl").click()

    def search(self, query: str):
        """ Performs a search using the search bar """
        self.page.wait_for_timeout(1000)
        self.page.get_by_placeholder("Busca por autor, título, género, ISBN").click()
        self.page.wait_for_timeout(1000)
        search_input = self.page.locator("[data-test=\"search-input\"]")
        search_input.click()
        search_input.clear()
        search_input.fill(query)
        search_input.press("Enter")