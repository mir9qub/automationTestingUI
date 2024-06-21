import time
from . Page import Page
from pageElements.ElementsPageLocators import *
from pageElements.texts.ElementsTexts import *
from selenium.webdriver.common.action_chains import ActionChains


class ElementsPage(Page):

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
        self.click_button(LCT_CHECKBOX_HOME_B)
        elements = self.find_elements(LCT_CHECKBOX_HOME_O)
        assert len(elements) > 0, f"Expected list of elements, Actual len is {len(elements)}"

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
        self.go_to_site()
        self.click_element(LCT_ELEMENTS_B)
        self.click_button(LCT_BUTTONS_B)
        actions = ActionChains(self.driver)
        self.double_click_button(LCT_DOUBLE_CLICK_B)
        self.check_visibility_by_locator(LCT_DOUBLE_CLICK_O)
        # right_click_element = self.find_element(LCT_RIGHT_CLICK_B)
        # actions.context_click(right_click_element).perform()
        # self.check_visibility_by_locator(LCT_RIGHT_CLICK_O)
        # self.click_button(LCT_DYNAMIC_CLICK_B)
        # self.check_visibility_by_locator(LCT_CLICK_O)
        time.sleep(2)

    def check_links(self):
        ...

    def check_broken_links(self):
        ...

    def check_upload_download(self):
        ...

    def check_dynamic_properties(self):
        ...


