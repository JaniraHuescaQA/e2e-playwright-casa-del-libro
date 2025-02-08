from pages.home_page import HomePage
from pages.header_page import HeaderPage
from pages.my_account_page import MyAccountPage
from pages.login_page import LoginPage

# SCENARIO 1 (login with invalid email)
def test_login_with_invalid_email(page):
    print("Given the user visits the homepage")
    home_page = HomePage(page)
    home_page.visit()

    print("And the user accepts the cookies")
    home_page.accept_cookies()

    print("And the user navigates to the login page")
    header_page = HeaderPage(page)
    header_page.go_to_my_account()

    my_account = MyAccountPage(page)
    my_account.go_to_login()

    print("When the user fills the signup form with invalid email")
    login_page = LoginPage(page)
    login_page.disable_hover_for_modals()
    login_page.fill_email("janirahuesc@gmail.com")  # Invalid email
    login_page.fill_password("ABCdef123!")
    login_page.click_login_button()

    print("Then the user should see an error message indicating that the email or password are invalid")
    login_page.get_error_message("Email o contraseña no válidos")

# SCENARIO 2 (login with empty password)
def test_login_with_empty_password(page):
    print("Given the user visits the homepage")
    home_page = HomePage(page)
    home_page.visit()

    print("And the user accepts the cookies")
    home_page.accept_cookies()

    print("And the user navigates to the login page")
    header_page = HeaderPage(page)
    header_page.go_to_my_account()

    my_account = MyAccountPage(page)
    my_account.go_to_login()

    print("When the user leaves the password field empty")
    login_page = LoginPage(page)
    login_page.disable_hover_for_modals()
    login_page.fill_email("janirahuesca@gmail.com")
    login_page.fill_password("") # Empty password
    login_page.click_login_button()

    print("Then the user should see an error message indicating that this field is mandatory")
    login_page.get_error_message("Este campo es obligatorio")