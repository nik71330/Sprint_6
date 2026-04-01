from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    @staticmethod
    def DATE_OPTION(day: str):
        return (By.XPATH, f"//div[contains(@class,'react-datepicker__day') and text()='{day}']")

    @staticmethod
    def METRO_OPTION(station_name):
        return (By.XPATH, f"//div[@class='select-search__select']//*[text()='{station_name}']")

    RENTAL_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")

    @staticmethod
    def RENTAL_OPTION(value):
        return (By.XPATH, f"//div[@class='Dropdown-option' and text()='{value}']")

    @staticmethod
    def COLOR(color: str):
        return (By.XPATH, f'//input[@id="{color}"]')

    NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")
    ORDER_BUTTON = (By.XPATH, "//*[contains(@class,'Order_Content')]//button[contains(normalize-space(.), 'Заказать')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(text(),'Заказ оформлен')]")
