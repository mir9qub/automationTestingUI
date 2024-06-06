from config.conftest import browser
from pages.ElementsPage import ElementsPage


def test_check_text_box(browser):
    elem_page = ElementsPage(browser)
    elem_page.check_text_box()


def test_check_checkbox(browser):
    elem_page = ElementsPage(browser)
    elem_page.check_checkbox()

def test_radio_button(browser):
    elem_page = ElementsPage(browser)
    elem_page.check_radio_button()


def test_check_buttons(browser):
    elem_page = ElementsPage(browser)
    elem_page.check_buttons()

