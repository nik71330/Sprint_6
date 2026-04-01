from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, base_url="https://qa-scooter.praktikum-services.ru"):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.base_url = base_url

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def open(self, url=None):
        self.driver.get(url or self.base_url)

    def get_current_url(self):
        return self.driver.current_url

    def get_text(self, locator):
        return self.wait_for_visible(locator).text

    def scroll_to_element(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        return element

    def click(self, locator):
        self.scroll_to_element(locator)
        self.wait_for_clickable(locator).click()

    def send_keys(self, locator, value):
        element = self.wait_for_clickable(locator)
        element.clear()
        element.send_keys(value)

    def switch_to_new_window(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(lambda d: d.current_url != "about:blank")
        return True

    def click_if_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
            return True
        except TimeoutException:
            return False

    def click_faq(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        width = element.size["width"]
        x_offset = -(width // 2) + 20

        ActionChains(self.driver) \
            .move_to_element_with_offset(element, x_offset, 0) \
            .click() \
            .perform()