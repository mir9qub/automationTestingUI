from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://85.192.34.140:8081/'

    def go_to_site(self):
        self.driver.get(self.base_url)

    def click_button(self, locator):
        return WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(locator)).click()

    def find_element(self, locator):
        return WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator: {locator}"
        )

    def click_element(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, key):
        self.find_element(locator).send_keys(key)

    def check_visibility_by_locator(self, locator):
        try:
            WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(locator))
            return True
        except Exception as exc:
            return exc

    def compare_texts(self, locator, expected_text):
        element = self.find_element(locator)
        assert element.text == expected_text, f"Element text: {element.text}, Expected text: {expected_text}"



