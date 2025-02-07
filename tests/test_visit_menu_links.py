from pages.header_page import HeaderPage
from pages.home_page import HomePage
from playwright.sync_api import Page

def test_visit_menu_links(page:Page):
    """
    Test to verify menu navigation functionality.
    """
    # Instantiate page objects
    home_page = HomePage(page)
    header_page = HeaderPage(page)

    print("Given the user visits 'La Casa del Libro' homepage")
    # Navigation to open the URL in the browser
    home_page.visit()

    print("And the user accepts the cookies")
    home_page.accept_cookies()

    print("When the user clicks on the 'Imprescindibles' link")
    header_page.click_menu_link("Imprescindibles", "Todo Imprescindibles")
    
    print("Then the user should be on 'Imprescindibles' page")
    header_page.verify_page("imprescindibles", "Libros imprescindibles | Casa del Libro", "Libros imprescindibles")
    
    print("When the user clicks on the 'Ficción' link")
    header_page.click_menu_link("Ficción", "Todo Ficción")

    print("Then the user should be on 'Ficción' page")
    header_page.verify_page("literatura", "Mejores libros de Literatura | Casa del Libro", "Libros de Literatura")

    print("When the user clicks on the 'No Ficción' link")
    header_page.click_menu_link("No Ficción", "Todo No Ficción")
    
    print("Then the user should be on 'No Ficción' page")
    header_page.verify_page("no-ficcion", "Libros de no ficción | Casa del Libro", "Libros de no ficción: autoayuda, ciencias, historia, cocina...")

    print("When the user clicks on the 'Infantil' link")
    header_page.click_menu_link("Infantil", "Todo Infantil")
    
    print("Then the user should be on 'Infantil' page")
    header_page.verify_page("infantil", "Los mejores Libros Infantiles | Casa del Libro", "Libros infantiles")

    print("When the user clicks on the 'Juvenil' link")
    header_page.click_menu_link("Juvenil", "Todo Juvenil")
    
    print("Then the user should be on 'Juvenil' page")
    header_page.verify_page("juvenil", "¿Qué libros leen los adolescentes? | Casa del Libro", "Libros para Jóvenes Lectores")

    print("When the user clicks on the 'Cómic y Manga' link")
    header_page.click_menu_link("Cómic y Manga", "Todo Cómic y Manga")
    
    print("Then the user should be on 'Cómic y Manga' page")
    header_page.verify_page("comics", "Cómics | Casa del Libro", "Cómics")

    print("When the user clicks on the 'English books' link")
    header_page.click_menu_link("English books", "Todo English books")

    print("Then the user should be on 'English books' page")
    header_page.verify_page("ingles", "Libros en Inglés | Casa del Libro", "Libros en Inglés")

    print("When the user clicks on the 'Llibres en català' link")
    header_page.click_menu_link("Llibres en català", "Todo Llibres en català")
    
    print("Then the user should be on 'Llibres en català' page")
    header_page.verify_page("catala", "Millors Llibres en català | Casa del Llibre", "Llibres en català")

    print("When the user clicks on the 'Papelería' link")
    header_page.click_menu_link("Papelería", "Todo Papelería")
    
    print("Then the user should be on 'Papelería' page")
    header_page.verify_page("papeleria", "Accesorios y complementos para la lectura | Casa del Libro", "Papelería y regalo")

    print("When the user clicks on the 'eBooks' link")
    header_page.click_menu_link("eBooks", "Todo eBooks")
    
    print("Then the user should be on 'eBooks' page")
    header_page.verify_page("ebooks", "Los mejores eBooks | Casa del Libro", "eBooks")

    print("When the user clicks on the 'Ofertas' link")
    header_page.click_menu_link("Ofertas")

    print("Then the user should be on 'Ofertas' page")
    header_page.verify_page("descuentos", "Los mejores descuentos y ofertas en libros | Casa del libro", "Libros en promoción")