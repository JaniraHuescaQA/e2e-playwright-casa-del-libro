from playwright.sync_api import Page, expect

class ShoppingCartPage:
    def __init__(self, page: Page):
        """ 
        Constructor to initialize the ShoppingCartPage class with the Playwright Page object.
        This allows us to interact with the webpage. 
        """
        self.page = page

    def verify_cart_section_is_visible(self):
        """Checks that the shopping cart section is visible."""
        expect(self.page.locator("div").filter(has_text="Tu cesta").nth(3)).to_be_visible()

    def verify_product_in_cart(self, product_name: str):
        """Checks that the added product appears in the cart."""
        expect(self.page.locator("#t-p-cl")).to_contain_text(product_name)

    def remove_product_from_cart(self):
        """Clicks on the trash icon to remove the product."""
        self.page.get_by_role("complementary").get_by_role("button").nth(1).click()

    def verify_product_not_in_cart(self):
        """Verifies that the product is no longer visible in the cart."""
        expect(self.page.locator("#t-p-cl")).not_to_be_visible()
    
    def verify_cart_is_empty(self):
        """Checks that the 'empty cart' message is displayed."""
        expect(self.page.locator("#c-v")).to_contain_text("Tu cesta está vacía")

    def close_shopping_cart_section(self):
        """Clicks on the close button to close the shopping cart section."""
        self.page.locator("#c-c").click()