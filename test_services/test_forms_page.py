from config.conftest import browser
from pages.FormsPage import FormsPage


def test_check_forms(browser):
    forms_page = FormsPage(browser)
    forms_page.check_form()

