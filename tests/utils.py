from playwright.sync_api import Page, expect
import re

def is_mobile(page:Page):
    desktop_size = 1024
    is_mobile = False
    if (page.viewport_size['width'] < desktop_size):
        is_mobile = True
    return is_mobile