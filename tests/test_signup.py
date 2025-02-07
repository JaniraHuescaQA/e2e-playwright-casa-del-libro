from pages.home_page import HomePage
from pages.header_page import HeaderPage
from pages.my_account_page import MyAccountPage
from pages.signup_page import SignupPage

def test_signup_with_invalid_email(page):
    print("Given the user visits the homepage")
    home_page = HomePage(page)
    home_page.visit()

    print("And the user accepts the cookies")
    home_page.accept_cookies()

    print("And the user navigates to the signup page")
    header_page = HeaderPage(page)
    header_page.go_to_my_account()

    my_account = MyAccountPage(page)
    my_account.go_to_signup()

    print("When the user fills the signup form with an invalid email")
    signup_page = SignupPage(page)
    signup_page.fill_first_name("Test Name")
    signup_page.fill_last_name("Test Surname")
    signup_page.fill_email("registertest.com")  # Invalid email
    signup_page.fill_password("Abcd1234!")
    signup_page.click_register_button()

    print("Then the user should see an error message indicating that the email must be valid")
    signup_page.get_error_message("El email debe ser válido")

def test_signup_with_empty_first_name(page):
    print("Given the user visits the homepage")
    home_page = HomePage(page)
    home_page.visit()

    print("And the user accepts the cookies")
    home_page.accept_cookies()

    print("And the user navigates to the signup page")
    header_page = HeaderPage(page)
    my_account = MyAccountPage(page)

    header_page.go_to_my_account()
    my_account.go_to_signup()

    print("When the user leaves the first name field empty")
    signup_page = SignupPage(page)
    signup_page.fill_first_name("")  # Empty name
    signup_page.fill_last_name("Test Surname")
    signup_page.fill_email("test@gmail.com")
    signup_page.fill_password("Abcd1234!")
    signup_page.click_register_button()

    print("Then the user should see an error message indicating that this field is mandatory")
    signup_page.get_error_message("Este campo es obligatorio")