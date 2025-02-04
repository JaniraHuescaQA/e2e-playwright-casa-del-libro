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
        # Small delay to ensure UI stability
        self.page.wait_for_timeout(1000)
        # Locate the element menu by locator, and click on it
        self.page.locator("button[name='menu']").click()

    def click_category(self, category_name: str):
        """Clicks on the main category considering mobile and desktop versions."""
        if utils.is_mobile(self.page):
            if category_name == "Ofertas":
                self.page.get_by_role("link", name=category_name, exact=True).click()
                return
            self.page.get_by_role("button", name=category_name, exact=True).first.click()
        else:
            # Small delay to ensure UI stability
            self.page.wait_for_timeout(1000)
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
        Handles menu clicks for both categories and subcategories.
        Args:
            category_name (str): The main category name to click.
            subcategory_name (str, optional): The subcategory name if needed.
        """
        if utils.is_mobile(self.page):
            self.open_menu()
        
        self.click_category(category_name)
        
        if utils.is_mobile(self.page):
            self.click_subcategory(subcategory_name)

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