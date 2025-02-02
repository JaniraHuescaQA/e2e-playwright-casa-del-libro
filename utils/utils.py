from playwright.sync_api import Page

def is_mobile(page) -> bool:
    """ 
    Checks if the current viewport size indicates a mobile device.
    Returns:
        bool: True if the viewport width is less than 1024px, otherwise False.
    """
    desktop_size = 1024
    return page.viewport_size['width'] < desktop_size