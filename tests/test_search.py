from playwright.sync_api import Page, expect

# SCENARIO 1 (valid search)
def test_valid_search(page:Page):
    print("Given the user visits signup page")
    # Navigation to open the URL in the browser
    page.goto("https://www.casadellibro.com/")

    print("When the user accepts the cookies")
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

    print("Then the user should be redirected to the page with its search") 
    # Verify that the query contains the search in the url
    expect(page).to_have_url("https://www.casadellibro.com/?query=harry%20potter")

    print("And the user should see a message indicating how many results there are with its search")
    # Verify that there are results for the search and that the message is visible
    expect(page.get_by_text(f"resultados para {content_searched}")).to_be_visible()

    print("And the user should see results containing its search")
    # Verify that the results shown are related to the search performed
    expect(page.locator("[data-test=\"base-grid\"]")).to_contain_text(content_searched)

# SCENARIO 2 (invalid search)
def test_valid_search(page:Page):
    print("Given the user visits signup page")
    # Navigation to open the URL in the browser
    page.goto("https://www.casadellibro.com/")

    print("When the user accepts the cookies")
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
    # Fill the search input with an invalid serach
    invalid_content_searched = ".."
    page.locator("[data-test=\"search-input\"]").fill(invalid_content_searched)

    print("And the user press 'Enter' in the keyboard")
    # Press intro
    page.locator("[data-test=\"search-input\"]").press("Enter")

    print("Then the user should be redirected to the page with its search")
    # Verify that the query contains the search in the url
    expect(page).to_have_url("https://www.casadellibro.com/?query=..")

    print("And the user should see a message indicating that no results were found")
    # Verify that a message indicating that there are no results is visible and contains the search performed
    expect(page.locator("[data-test=\"no-results-message\"]")).to_be_visible()
    expect(page.locator("[data-test=\"no-results-message\"]")).to_contain_text("No se han encontrado resultados para \"..\"")