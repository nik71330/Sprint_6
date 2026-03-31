from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
import allure


class HomePage(BasePage):

    def click_order_top(self):
        with allure.step("Клик по верхней кнопке 'Заказать'"):
            self.click(HomePageLocators.ORDER_BUTTON_TOP)

    def click_order_bottom(self):
        with allure.step("Клик по нижней кнопке 'Заказать'"):
            element = self.wait_for_visible(HomePageLocators.ORDER_BUTTON_BOTTOM)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def click_samokat_logo(self):
        with allure.step("Клик по логотипу 'Самокат'"):
            self.click(HomePageLocators.SAMOKAT_LOGO)

    def click_yandex_logo(self):
        with allure.step("Клик по логотипу 'Яндекс'"):
            self.click(HomePageLocators.YANDEX_LOGO)

    def is_on_main_page(self) -> bool:
        with allure.step("Проверка, что открыта главная страница 'Самокат'"):
            current = self.get_current_url().rstrip('/')
            return current.startswith(self.base_url.rstrip('/'))

    def click_question_by_text(self, text: str):
        with allure.step(f"Клик по вопросу FAQ: {text}"):
            locator = HomePageLocators.QUESTION_BY_TEXT(text)
            element = self.wait_for_visible(locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def get_answer_text_by_text(self, question: str, answer: str) -> str:
        with allure.step(f"Получение ответа для вопроса: {question}"):
            locator = HomePageLocators.ANSWER_BY_QA_TEXT(question, answer)
            element = self.wait_for_visible(locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            return element.text
