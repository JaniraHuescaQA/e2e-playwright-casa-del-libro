from playwright.sync_api import Page, expect
import utils

# SCENARIO 1 (searching an item, adding it to the shopping cart and removing it from the shopping cart)
def test_search_add_remove_item_to_cart(page:Page):
    print("Given the user visits 'La Casa del Libro' homepage")
    # Navigation to open the URL in the browser
    utils.visit_homepage(page)

    print("And the user accepts the cookies")
    utils.accept_cookies(page)

    print("When the user performs a search")
    # Locate the element by placeholder and click on it
    page.wait_for_timeout(1000)
    page.get_by_placeholder("Busca por autor, título, género, ISBN").click()
    # Locate the element by locator and click on it
    page.wait_for_timeout(1000)
    page.locator("[data-test=\"search-input\"]").click()
    # Locate the element by locator and clear the content
    page.locator("[data-test=\"search-input\"]").clear()
    # Fill the search input with an valid search
    valid_content_searched = "harry potter"
    page.locator("[data-test=\"search-input\"]").fill(valid_content_searched)
    # Press intro
    page.locator("[data-test=\"search-input\"]").press("Enter")

    if not (utils.is_mobile(page)):
        print("Then the user should see a message indicating how many results there are with its search")
        # Verify that there are results for the search and that the message is visible
        expect(page.get_by_text(f"resultados para {valid_content_searched}")).to_be_visible()

    print("And the user should see results containing its search")
    # Verify that the results shown are related to the search performed
    expect(page.locator("[data-test=\"base-grid\"]")).to_contain_text(valid_content_searched)

    print("When the user clicks on the desired result")
    # Click on one of the results, in this case 'HARRY POTTER Y LA PIEDRA FILOSOFAL'
    page.get_by_role("link", name="HARRY POTTER Y LA PIEDRA FILOSOFAL", exact=True).click()

    print("And the user clicks on the button indicating the adding to cart action")
    # Click on the 'Add to cart' button
    page.get_by_role("button", name="Añadir a la cesta").first.click()

    print("Then the user should see the shopping cart section")
    # Verify that the content of shopping cart is visible
    expect(page.locator("div").filter(has_text="Tu cesta").nth(3)).to_be_visible()

    print("And the user should see that the item selected has been added to the shopping cart")
    # Verify that the item that there is in the shopping cart is the item selected
    expect(page.locator("#t-p-cl")).to_contain_text("HARRY POTTER Y LA PIEDRA FILOSOFAL")

    print("When the user clicks on the trash icon")
    # Locate the trash icon and click on it
    page.get_by_role("complementary").get_by_role("button").nth(1).click()

    print("Then the user should not see the item previously selected")
    # Verify that the item previously selected is not visible
    expect(page.locator("#t-p-cl")).not_to_be_visible

    print("And the user should see a message indicating that the cart is empty")
    # Verify that a message indicating the emptiness of the shopping cart is displayed
    expect(page.locator("#c-v")).to_contain_text("Tu cesta está vacía")