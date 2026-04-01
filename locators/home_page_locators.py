from selenium.webdriver.common.by import By


class HomePageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(text(), 'Заказать')]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")
    SAMOKAT_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")

    @staticmethod
    def QUESTION_BY_TEXT(text):
        return (By.XPATH, f"//div[@class='accordion__button' and text()='{text}']")

    @staticmethod
    def ANSWER_BY_QA_TEXT(question, answer):
        return (
            By.XPATH,
            f"//div[@class='accordion__button' and text()='{question}']/parent::div/following-sibling::div//p[text()='{answer}']"
        )