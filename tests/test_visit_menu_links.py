from playwright.sync_api import Page
from pages.header_page import HeaderPage
from pages.home_page import HomePage

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

    # Define test cases with category and expected page details
    test_cases = [
        ("Imprescindibles", "Todo Imprescindibles", "imprescindibles", "Libros imprescindibles | Casa del Libro", "Libros imprescindibles"),
        ("Ficción", "Todo Ficción", "literatura", "Mejores libros de Literatura | Casa del Libro", "Libros de Literatura"),
        ("No Ficción", "Todo No Ficción", "no-ficcion", "Libros de no ficción | Casa del Libro", "Libros de no ficción: autoayuda, ciencias, historia, cocina..."),
        ("Infantil", "Todo Infantil", "infantil", "Los mejores Libros Infantiles | Casa del Libro", "Libros infantiles"),
        ("Juvenil", "Todo Juvenil", "juvenil", "¿Qué libros leen los adolescentes? | Casa del Libro", "Libros para Jóvenes Lectores"),
        ("Cómic y Manga", "Todo Cómic y Manga", "comics", "Cómics | Casa del Libro", "Cómics"),
        ("English books", "Todo English books", "ingles", "Libros en Inglés | Casa del Libro", "Libros en Inglés"),
        ("Llibres en català", "Todo Llibres en català", "catala", "Millors Llibres en català | Casa del Llibre", "Llibres en català"),
        ("Papelería", "Todo Papelería", "papeleria", "Accesorios y complementos para la lectura | Casa del Libro", "Papelería y regalo"),
        ("eBooks", "Todo eBooks", "ebooks", "Los mejores eBooks | Casa del Libro", "eBooks"),
    ]

    # Iterate through each test case
    for category, subcategory, url_keyword, title, heading in test_cases:
        print(f"When the user clicks on the '{category}' link")
        
        header_page.click_menu_link(category, subcategory)
        
        print(f"Then the user should be on '{category}' page")
        header_page.verify_page(url_keyword, title, heading)
    
     # Special case: "Ofertas" (no subcategory in mobile)
    print("When the user clicks on the 'Ofertas' link")
    header_page.click_menu_link("Ofertas")

    print("Then the user should be on 'Ofertas' page")
    header_page.verify_page("descuentos", "Los mejores descuentos y ofertas en libros | Casa del libro", "Libros en promoción")