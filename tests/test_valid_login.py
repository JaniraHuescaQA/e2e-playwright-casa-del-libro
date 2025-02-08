from pages.home_page import HomePage
from pages.header_page import HeaderPage
from pages.my_account_page import MyAccountPage
from pages.login_page import LoginPage

def test_succesful_login(page):
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

    print("When the user fills the signup form with valid email and password")
    login_page = LoginPage(page)
    login_page.fill_email("janirahuesca@gmail.com")  # Invalid email
    login_page.fill_password("ABCdef123!")
    login_page.click_login_button()

    print("Then the user should be logged in")
    login_page.verify_login()