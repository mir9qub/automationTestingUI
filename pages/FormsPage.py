import time

from .Page import Page
from pageElements.FormsPageLocators import *


class FormsPage(Page):

    def check_form(self):
        self.go_to_site()
        self.click_button(LCT_FORMS_B)
        self.click_button(LCT_FORMS_PRACTICE_B)
        # self.send_keys(LCT_FIRSTNAME_I, "Adam")
        # self.send_keys(LCT_LASTNAME_I, "Emers")
        # self.send_keys(LCT_USER_EMAIL_I, "adamemers@gmail.com")
        # self.click_button(LCT_GENDER_MALE_I)
        # self.send_keys(LCT_USER_MOBILE_I, "7777777777")
        self.click_button(LCT_BIRTH_I)
        # self.scroll_to_element(LCT_SELECT_MONTH)
        self.select_by_value(LCT_SELECT_MONTH, "May")
        time.sleep(2)