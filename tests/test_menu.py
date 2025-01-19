from playwright.sync_api import Page, expect

def test_visit_menu_links(page:Page):
    print("Given the user visits 'La Casa del Libro' homepage")
    # Navigation to open the URL in the browser
    page.goto("https://www.casadellibro.com/")

    print("When the user accepts the cookies")
    # Locate the element by role (button) to accept the cookies
    page.get_by_role("button", name="Aceptar")

    print("When the user clicks on the 'Imprescindibles' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="Imprescindibles", exact=True).click()

    print("When the user clicks on the 'Ficción' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="Ficción", exact=True).first.click()

    print("When the user clicks on the 'No Ficción' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="No Ficción", exact=True).click()
    
    print("When the user clicks on the 'Infantil' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="Infantil", exact=True).first.click()

    print("When the user clicks on the 'Juvenil' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="Juvenil", exact=True).first.click()

    print("When the user clicks on the 'Cómic y Manga' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="Cómic y Manga", exact=True).click()

    print("When the user clicks on the 'English books' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="English books", exact=True).first.click()

    print("When the user clicks on the 'Llibres en català' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="Llibres en català", exact=True).first.click()
    
    print("When the user clicks on the 'Papelería' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="Papelería", exact=True).first.click()

    print("When the user clicks on the 'eBooks' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="eBooks", exact=True).nth(2).click()

    print("When the user clicks on the 'Ofertas' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="Ofertas", exact=True).click()