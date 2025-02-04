#from playwright.sync_api import Page, expect
#import tests.utils.utils as utils
#
## SCENARIO 1 (invalid search)
#def test_invalid_search(page:Page):
#    print("Given the user visits 'La Casa del Libro' homepage")
#    # Navigation to open the URL in the browser
#    utils.visit_homepage(page)
#
#    print("And the user accepts the cookies")
#    utils.accept_cookies(page)
#
#    print("When the user performs a search")
#    # Locate the element by placeholder and click on it
#    page.wait_for_timeout(1000)
#    page.get_by_placeholder("Busca por autor, título, género, ISBN").click()
#    # Locate the element by locator and click on it
#    page.wait_for_timeout(1000)
#    page.locator("[data-test=\"search-input\"]").click()
#    # Locate the element by locator and clear the content
#    page.locator("[data-test=\"search-input\"]").clear()
#    # Fill the search input with an invalid search
#    invalid_content_searched = ".."
#    page.locator("[data-test=\"search-input\"]").fill(invalid_content_searched)
#    # Press intro
#    page.locator("[data-test=\"search-input\"]").press("Enter")
#
#    print("Then the user should see a message indicating that no results were found")
#    # Verify that a message indicating that there are no results is visible
#    expect(page.locator("[data-test=\"no-results-message\"]")).to_be_visible()
#    expect(page.locator("[data-test=\"no-results-message\"]")).to_contain_text("No se han encontrado resultados para ")