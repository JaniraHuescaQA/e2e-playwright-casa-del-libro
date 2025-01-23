from playwright.sync_api import Page, expect

# SCENARIO 1 (adding an item to the shopping cart)
def test_add_item_to_cart(page:Page):
    print("Given the user visits signup page")
    # Navigation to open the URL in the browser
    page.goto("https://www.casadellibro.com/")

    print("And the user accepts the cookies")
    # Wait until the banner to accept the cookies appears
    page.wait_for_selector("button:has-text('Aceptar')")
    # Locate the element by role (button) to accept the cookies and click on it
    page.get_by_role("button", name="Aceptar").click()

    print("And the user clicks on the search bar")
    # Locate the element by placeholder and click on it
    page.get_by_placeholder("Busca por autor, título, género, ISBN").click()

    print("And the user clicks on the search input")
    # Locate the element by locator and click on it
    page.locator("[data-test=\"search-input\"]").click()
    # Locate the element by locator and clear the content
    page.locator("[data-test=\"search-input\"]").clear()

    print("And the user fills the search input with the search that want to perform")
    # Fill the search input with a valid search
    content_searched = "harry potter"
    page.locator("[data-test=\"search-input\"]").fill(content_searched)

    print("And the user press 'Enter' in the keyboard")
    # Press intro
    page.locator("[data-test=\"search-input\"]").press("Enter")

    print("And the user is redirected to the page with its search")
    # Verify that the query contains the search
    expect(page).to_have_url("https://www.casadellibro.com/?query=harry%20potter")

    print("When the user clicks on the desired result")
    # Click on one of the results, in this case 'HARRY POTTER Y LA PIEDRA FILOSOFAL'
    page.get_by_role("link", name="HARRY POTTER Y LA PIEDRA FILOSOFAL", exact=True).click()

    print("And the user clicks on the button indicating the adding to cart action")
    # Click on the 'Add to cart' button
    page.get_by_role("button", name="Añadir a la cesta").click()

    print("Then the user should see the shopping cart section")
    # Verify that the content of shopping cart is visible
    expect(page.locator("div").filter(has_text="Tu cesta").nth(3)).to_be_visible()

    print("And the user should see that the item selected has been added to the shopping cart")
    # Verify that the item that there is in the shopping cart is the item selected
    expect(page.locator("#t-p-cl")).to_contain_text("HARRY POTTER Y LA PIEDRA FILOSOFAL")

    # SCENARIO 2 (removing an item from the shopping cart)
def test_remove_item_from_cart(page:Page):
    print("Given the user visits signup page")
    # Navigation to open the URL in the browser
    page.goto("https://www.casadellibro.com/")

    print("And the user accepts the cookies")
    # Wait until the banner to accept the cookies appears
    page.wait_for_selector("button:has-text('Aceptar')")
    # Locate the element by role (button) to accept the cookies and click on it
    page.get_by_role("button", name="Aceptar").click()

    print("And the user clicks on the search bar")
    # Locate the element by placeholder and click on it
    page.get_by_placeholder("Busca por autor, título, género, ISBN").click()

    print("And the user clicks on the search input")
    # Locate the element by locator and click on it
    page.locator("[data-test=\"search-input\"]").click()
    # Locate the element by locator and clear the content
    page.locator("[data-test=\"search-input\"]").clear()

    print("And the user fills the search input with the search that want to perform")
    # Fill the search input with a valid search
    content_searched = "harry potter"
    page.locator("[data-test=\"search-input\"]").fill(content_searched)

    print("And the user press 'Enter' in the keyboard")
    # Press intro
    page.locator("[data-test=\"search-input\"]").press("Enter")

    print("And the user is redirected to the page with its search")
    # Verify that the query contains the search
    expect(page).to_have_url("https://www.casadellibro.com/?query=harry%20potter")

    print("And the user clicks on the desired result")
    # Click on one of the results, in this case 'HARRY POTTER Y LA PIEDRA FILOSOFAL'
    page.get_by_role("link", name="HARRY POTTER Y LA PIEDRA FILOSOFAL", exact=True).click()

    print("And the user clicks on the button indicating the adding to cart action")
    # Click on the 'Add to cart' button
    page.get_by_role("button", name="Añadir a la cesta").click()

    print("And the user sees the shopping cart section")
    # Verify that the content of shopping cart is visible
    expect(page.locator("div").filter(has_text="Tu cesta").nth(3)).to_be_visible()

    print("And the user sees that the item selected has been added to the shopping cart")
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