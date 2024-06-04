import time
from . BasePage import BasePage
from pageElements.ElementsLocators import *
from pageElements.texts.ElementsTexts import *


class ElementsPage(BasePage):

    def check_text_box(self):
        self.go_to_site()
        self.click_element(LCT_ELEMENTS_B)
        self.click_button(LCT_TEXT_BOX_B)
        self.send_keys(LCT_FULL_NAME_I, FULL_NAME)
        self.send_keys(LCT_EMAIL_I, EMAIL)
        self.send_keys(LCT_CURRENT_ADDRESS_I, CURRENT_ADDRESS)
        self.send_keys(LCT_PERMANENT_ADDRESS_I, PERMANENT_ADDRESS)
        self.click_button(LCT_SUBMIT_B)
        assert self.check_visibility_by_locator(LCT_TEXT_BOX_O) is True, f"Element is not visible"

    def check_checkbox(self):
        self.go_to_site()
        self.click_element(LCT_ELEMENTS_B)
        self.click_button(LCT_CHECK_BOX_B)

    def check_radio_button(self):
        self.go_to_site()
        self.click_element(LCT_ELEMENTS_B)
        self.click_button(LCT_RADIO_BUTTON_B)
        self.click_button(LCT_RB_YES_B)
        self.compare_texts(LCT_RADIO_BUTTON_O, "Yes")
        self.click_button(LCT_RB_IMP_B)
        self.compare_texts(LCT_RADIO_BUTTON_O, "Impressive")
        self.click_button(LCT_RB_NO_B)
        self.compare_texts(LCT_RADIO_BUTTON_O, "Impressive")

    def check_web_tables(self):
        ...

    def check_buttons(self):
        ...

    def check_links(self):
        ...

    def check_broken_links(self):
        ...

    def check_upload_download(self):
        ...

    def check_dynamic_properties(self):
        ...


