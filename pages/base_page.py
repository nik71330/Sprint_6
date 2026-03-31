import os
from typing import Optional

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, base_url: Optional[str] = None, timeout: Optional[int] = None):
        self.driver = driver
        self.base_url = base_url or os.getenv("BASE_URL", "").rstrip("/")
        if not self.base_url:
            raise RuntimeError("BASE_URL is not set. Provide it via .env or constructor.")
        self.timeout = int(timeout or os.getenv("DEFAULT_WAIT"))
        self.wait = WebDriverWait(self.driver, self.timeout)

    def open(self):
        self.driver.get(self.base_url)

    def presence(self, locator):
        return self.wait.until(
            expected_conditions.presence_of_element_located(locator)
        )

    def clickable(self, locator):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(locator)
        )

    def click(self, locator):
        for _ in range(3):
            try:
                # получаем свежий элемент и ждём кликабельности
                btn = self.clickable(locator)
                btn.click()
                return
            except StaleElementReferenceException:
                # пробуем заново получить элемент
                continue
        # последний шанс: свежий элемент + JS-клик
        btn = self.presence(locator)
        self.driver.execute_script("arguments[0].click();", btn)
        return self

    def get_current_url(self):
        return self.driver.current_url

    def send_keys(self, locator, value: str):
        element = self.wait_for_visible(locator)
        element.send_keys(value)
        return self

    def wait_for_visible(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_url(self, url):
        try:
            return self.wait.until(expected_conditions.url_to_be(url))
        except TimeoutException:
            return False

    def wait_for_url_contains(self, substring):
        try:
            return self.wait.until(expected_conditions.url_contains(substring))
        except TimeoutException:
            return False

    def switch_to_new_window(self):
        handles = self.driver.window_handles
        if len(handles) > 1:
            self.driver.switch_to.window(handles[1])
            return True
        return False

    def get_text(self, root, locator) -> str:
        return root.find_element(*locator).text.strip()
