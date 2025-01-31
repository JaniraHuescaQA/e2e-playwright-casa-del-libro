from playwright.sync_api import Page, expect
import re

def visit_homepage(page: Page):
    page.goto("https://www.casadellibro.com")

def accept_cookies(page: Page):
    # Wait until the banner to accept the cookies appears
    page.wait_for_selector("button:has-text('Aceptar')")
    # Locate the element by role (button) to accept the cookies and click on it
    page.get_by_role("button", name="Aceptar").click()

def is_mobile(page:Page):
    desktop_size = 1024
    is_mobile = False
    if (page.viewport_size['width'] < desktop_size):
        is_mobile = True
    return is_mobile