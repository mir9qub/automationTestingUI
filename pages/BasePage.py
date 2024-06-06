from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://85.192.34.140:8081/'

    def go_to_site(self):
        self.driver.get(self.base_url)

    def click_button(self, locator):
        return WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(locator)).click()

    def double_click_button(self, locator):
        action_chains = ActionChains(self.driver)
        action_chains.double_click(WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(locator)).click()).perform()

    def find_element(self, locator):
        return WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator: {locator}"
        )

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 7).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find element by locator: {locator}"
        )

    def click_element(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, key):
        self.find_element(locator).send_keys(key)

    def check_visibility_by_locator(self, locator):
        WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(locator))

    def compare_texts(self, locator, expected_text):
        element = self.find_element(locator)
        assert element.text == expected_text, f"Element text: {element.text}, Expected text: {expected_text}"

    def check_element_has_text(self, locator):
        pass