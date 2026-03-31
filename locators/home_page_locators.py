from selenium.webdriver.common.by import By


class HomePageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")
    SAMOKAT_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]//img")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]//img")
    QUESTION_BY_TEXT = staticmethod(
        lambda text: (By.XPATH, f"//div[@class='accordion__button' and text()='{text}']"))

    @staticmethod
    def ANSWER_BY_QA_TEXT(question: str, answer: str):
        return (
            By.XPATH,
            f"//div[@class='accordion__button' and normalize-space(text())='{question}']/../..//*[normalize-space(text())='{answer}']"
        )
