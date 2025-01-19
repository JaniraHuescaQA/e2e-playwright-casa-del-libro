from playwright.sync_api import Page, expect
import re

def test_visit_menu_links(page:Page):
    print("Given the user visits 'La Casa del Libro' homepage")
    # Navigation to open the URL in the browser
    page.goto("https://www.casadellibro.com/")

    print("When the user accepts the cookies")
    # Locate the element by role (button) to accept the cookies
    page.get_by_role("button", name="Aceptar")

    print("And the user clicks on the 'Imprescindibles' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="Imprescindibles", exact=True).click()
    print("Then the user should be on 'Imprescindibles' page")
    # Check that URL page has the exact URL
    expect(page).to_have_url("https://www.casadellibro.com/libros-imprescindibles")
    # Check that URL page contains the word 'imprescindibles'
    expect(page).to_have_url(re.compile("imprescindibles"))
    # Check that title page has the exact text 'Libros imprescindibles | Casa del Libro'
    expect(page).to_have_title("Libros imprescindibles | Casa del Libro")
    # Locate the element of type 'p' and filter by text 'Libros imprescindibles', and check that is visibe
    expect(page.locator("p").filter(has_text="Libros imprescindibles")).to_be_visible

    print("When the user clicks on the 'Ficción' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="Ficción", exact=True).first.click()
    print("Then the user should be on 'Ficción' page")
    # Check that URL page has the exact URL
    expect(page).to_have_url("https://www.casadellibro.com/libros/literatura/121000000")
    # Check that URL page contains the word 'literatura'
    expect(page).to_have_url(re.compile("literatura"))
    # Check that title page has the exact text 'Mejores libros de Literatura | Casa del Libro'
    expect(page).to_have_title("Mejores libros de Literatura | Casa del Libro")
    # Locate the element by role (heading) and for exact text, and check that is visibe
    expect(page.get_by_role("heading", name="Libros de Literatura", exact=True)).to_be_visible

    print("When the user clicks on the 'No Ficción' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="No Ficción", exact=True).click()
    print("Then the user should be on 'No Ficción' page")
    # Check that URL page has the exact URL
    expect(page).to_have_url("https://www.casadellibro.com/libros-no-ficcion")
    # Check that URL page contains the word 'no ficcion'
    expect(page).to_have_url(re.compile("no-ficcion"))
    # Check that title page has the exact text 'Libros de no ficción | Casa del Libro'
    expect(page).to_have_title("Libros de no ficción | Casa del Libro")
    # Locate the element by role (heading) and for text, and check that is visibe
    expect(page.get_by_role("heading", name="Libros de no ficción")).to_be_visible

    print("When the user clicks on the 'Infantil' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="Infantil", exact=True).first.click()
    print("Then the user should be on 'Infantil' page")
    # Check that URL page has the exact URL
    expect(page).to_have_url("https://www.casadellibro.com/libros/infantil/117000000")
    # Check that URL page contains the word 'infantil'
    expect(page).to_have_url(re.compile("infantil"))
    # Check that title page has the exact text 'Los mejores Libros Infantiles | Casa del Libro'
    expect(page).to_have_title("Los mejores Libros Infantiles | Casa del Libro")
    # Locate the element by role (heading) and for exact text, and check that is visibe
    expect(page.get_by_role("heading", name="Libros infantiles", exact=True)).to_be_visible

    print("When the user clicks on the 'Juvenil' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="Juvenil", exact=True).first.click()
    print("Then the user should be on 'Juvenil' page")
    # Check that URL page has the exact URL
    expect(page).to_have_url("https://www.casadellibro.com/libros/juvenil/473000000")
    # Check that URL page contains the word 'juvenil'
    expect(page).to_have_url(re.compile("juvenil"))
    # Check that title page has the exact text '¿Qué libros leen los adolescentes? | Casa del Libro'
    expect(page).to_have_title("¿Qué libros leen los adolescentes? | Casa del Libro")
    # Locate the element by role (heading) and for text, and check that is visibe
    expect(page.get_by_role("heading", name="Libros para Jóvenes")).to_be_visible

    print("When the user clicks on the 'Cómic y Manga' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="Cómic y Manga", exact=True).click()
    print("Then the user should be on 'Cómic y Manga' page")
    # Check that URL page has the exact URL
    expect(page).to_have_url("https://www.casadellibro.com/libros/comics/411000000")
    # Check that URL page contains the word 'comics'
    expect(page).to_have_url(re.compile("comics"))
    # Check that title page has the exact text 'Cómics | Casa del Libro'
    expect(page).to_have_title("Cómics | Casa del Libro")
    # Locate the element by role (heading) and for text, and check that is visibe
    expect(page.get_by_role("heading", name="Cómics")).to_be_visible

    print("When the user clicks on the 'English books' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="English books", exact=True).first.click()
    print("Then the user should be on 'English books' page")
    # Check that URL page has the exact URL
    expect(page).to_have_url("https://www.casadellibro.com/libros-en-ingles")
    # Check that URL page contains the word 'ingles'
    expect(page).to_have_url(re.compile("ingles"))
    # Check that title page has the exact text 'Libros en Inglés | Casa del Libro'
    expect(page).to_have_title("Libros en Inglés | Casa del Libro")
    # Locate the element by role (heading) and for exact text, and check that is visibe
    expect(page.get_by_role("heading", name="Libros en Inglés", exact=True)).to_be_visible

    print("When the user clicks on the 'Llibres en català' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="Llibres en català", exact=True).first.click()
    print("Then the user should be on 'Llibres en català' page")
    # Check that URL page has the exact URL
    expect(page).to_have_url("https://www.casadellibro.com/llibres-en-catala")
    # Check that URL page contains the word 'catala'
    expect(page).to_have_url(re.compile("catala"))
    # Check that title page has the exact text 'Millors Llibres en català | Casa del Llibre'
    expect(page).to_have_title("Millors Llibres en català | Casa del Llibre")
    # Locate the element by role (heading) and for exact text, and check that is visibe
    expect(page.get_by_role("heading", name="Llibres en català", exact=True)).to_be_visible

    print("When the user clicks on the 'Papelería' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="Papelería", exact=True).first.click()
    print("Then the user should be on 'Papelería' page")
    # Check that URL page has the exact URL
    expect(page).to_have_url("https://www.casadellibro.com/papeleria")
    # Check that URL page contains the word 'papeleria'
    expect(page).to_have_url(re.compile("papeleria"))
    # Check that title page has the exact text 'Accesorios y complementos para la lectura | Casa del Libro'
    expect(page).to_have_title("Accesorios y complementos para la lectura | Casa del Libro")
    # Locate the element by role (heading) and for exact text, and check that is visibe
    expect(page.get_by_role("heading", name="Papelería y regalo", exact=True)).to_be_visible

    print("When the user clicks on the 'eBooks' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="eBooks", exact=True).nth(2).click()
    print("Then the user should be on 'eBooks' page")
    # Check that URL page has the exact URL
    expect(page).to_have_url("https://www.casadellibro.com/ebooks")
    # Check that URL page contains the word 'ebooks'
    expect(page).to_have_url(re.compile("ebooks"))
    # Check that title page has the exact text 'Los mejores eBooks | Casa del Libro'
    expect(page).to_have_title("Los mejores eBooks | Casa del Libro")
    # Locate the element by role (heading) and for text, and check that is visibe
    expect(page.get_by_role("heading", name="eBooks")).to_be_visible

    print("When the user clicks on the 'Ofertas' link")
    # Locate the element by role (link) and for exact text, and click on it
    page.get_by_role("link", name="Ofertas", exact=True).click()
    print("Then the user should be on 'Ofertas' page")
    # Check that URL page has the exact URL
    expect(page).to_have_url("https://www.casadellibro.com/libros-descuentos-especiales")
    # Check that URL page contains the word 'descuentos'
    expect(page).to_have_url(re.compile("descuentos"))
    # Check that title page has the exact text 'Los mejores descuentos y ofertas en libros | Casa del libro'
    expect(page).to_have_title("Los mejores descuentos y ofertas en libros | Casa del libro")
    # Locate the element of type 'p' and filter by text 'Libros en promoción', and check that is visibe
    expect(page.locator("p").filter(has_text="Libros en promoción")).to_be_visible