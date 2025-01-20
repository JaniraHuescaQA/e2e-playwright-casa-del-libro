from playwright.sync_api import Page, expect
import uuid

# SCENARIO 1 (invalid email)
def test_signup_with_invalid_email(page:Page):
    print("Given the user visits signup page")
    # Navigation to open the URL in the browser
    page.goto("https://www.casadellibro.com/register-access")

    print("When the user accepts the cookies")
    # Wait until the banner to accept the cookies appears
    page.wait_for_selector("button:has-text('Aceptar')")
    # Locate the element by role (button) to accept the cookies and click on it
    page.get_by_role("button", name="Aceptar").click()

    print("And the user fills the first name with a valid name")
    # Clear the first name field
    page.get_by_label("Nombre*").clear()
    # Fill the field with a valid name
    name = "Test Name"
    page.get_by_label("Nombre*").fill(name)

    print("And the user fills the last name with a valid surname")
    # Clear the last name field
    page.get_by_label("Apellidos*").clear()
    # Fill the field with a valid last name
    surname = "Test Surname"
    page.get_by_label("Apellidos*").fill(surname)

    print("And the user fills the email with an invalid email")
    # Clear the email field
    page.get_by_label("Email*").clear()
    # Fill the field with an invalid email
    invalid_email = "registertest.com"
    page.get_by_label("Email*").fill(invalid_email)

    print("And the user fills the email with a valid password")
    # Clear the password field
    page.get_by_label("Contraseña*").clear()
    # Fill the field with a valid password
    password = "Abcd1234!"
    page.get_by_label("Contraseña*").fill(password)

    print("And the user clicks on the register button")
    # Locate the element by role (button) to click on it
    page.get_by_role("button", name="Registrarme").click()

    print("Then the user should be an error message")
    # Locate the element by text, and check that is visibe 
    expect(page.get_by_text("El email debe ser válido", exact=True)).to_be_visible()

# SCENARIO 2 (valid data)
def generate_random_email():
    unique_text = uuid.uuid4().hex
    random_email = unique_text + "@test.com"
    return random_email

def test_signup_with_valid_data(page:Page):
    print("Given the user visits signup page")
    # Navigation to open the URL in the browser
    page.goto("https://www.casadellibro.com/register-access")

    print("When the user accepts the cookies")
    # Wait until the banner to accept the cookies apppears
    page.wait_for_selector("button:has-text('Aceptar')")
    # Locate the element by role (button) to accept the cookies
    page.get_by_role("button", name="Aceptar").click()

    print("And the user fills the first name with a valid name")
    # Clear the first name field
    page.get_by_label("Nombre*").clear()
    # Fill the field with a valid name
    name = "Test Name"
    page.get_by_label("Nombre*").fill(name)

    print("And the user fills the last name with a valid surname")
    # Clear the last name field
    page.get_by_label("Apellidos*").clear()
    # Fill the field with a valid last name
    surname = "Test Surname"
    page.get_by_label("Apellidos*").fill(surname)

    print("And the user fills the email with a valid email")
    # Clear the email field
    page.get_by_label("Email*").clear()
    # Fill the field with a random valid email
    email = generate_random_email()
    page.get_by_label("Email*").fill(email)

    print("And the user fills the email with a valid password")
    # Clear the password field
    page.get_by_label("Contraseña*").clear()
    # Fill the field with a valid password
    password = "Abcd1234!"
    page.get_by_label("Contraseña*").fill(password)

    print("And the user clicks on the register button")
    # Locate the element by role (button) to click on it
    page.get_by_role("button", name="Registrarme").click()

    print("Then the user should be on 'Registry ok' page")
    ## Check that URL page has the exact URL
    expect(page).to_have_url("https://www.casadellibro.com/registry-ok")
    # Locate the element by role (heading) and for exact text, and check that is visibe
    expect(page.get_by_role("heading", name=f"Gracias {name}", exact=True)).to_be_visible