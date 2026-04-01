import allure
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    def open(self, url=None):
        super().open(url)
        self.click_if_present(HomePageLocators.COOKIE_ACCEPT_BUTTON)

    def click_order_top(self):
        with allure.step("Клик по верхней кнопке 'Заказать'"):
            self.click(HomePageLocators.ORDER_BUTTON_TOP)

    def click_order_bottom(self):
        with allure.step("Клик по нижней кнопке 'Заказать'"):
            self.click(HomePageLocators.ORDER_BUTTON_BOTTOM)

    def click_samokat_logo(self):
        with allure.step("Клик по логотипу 'Самокат'"):
            self.click(HomePageLocators.SAMOKAT_LOGO)

    def click_yandex_logo(self):
        with allure.step("Клик по логотипу 'Яндекс'"):
            self.click(HomePageLocators.YANDEX_LOGO)

    def is_on_main_page(self) -> bool:
        with allure.step("Проверка главной страницы"):
            return self.get_current_url().startswith(self.base_url)

    def click_question_by_text(self, text):
        with allure.step(f"Клик по вопросу: {text}"):
            locator = HomePageLocators.QUESTION_BY_TEXT(text)
            self.click_faq(locator)

    def get_answer_text_by_text(self, question, answer):
        with allure.step(f"Получение ответа: {question}"):
            locator = HomePageLocators.ANSWER_BY_QA_TEXT(question, answer)
            return self.get_text(locator)