from selenium.webdriver.support import expected_conditions

import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def fill_personal_data_form(self, first_name, last_name, address, metro_station, phone, *args, **kwargs):
        with allure.step(f"Заполнение личных данных: {first_name} {last_name}, {address}, {metro_station}, {phone}"):
            self.send_keys(OrderPageLocators.FIRST_NAME, first_name)
            self.send_keys(OrderPageLocators.LAST_NAME, last_name)
            self.send_keys(OrderPageLocators.ADDRESS, address)
            self.click(OrderPageLocators.METRO_STATION)
            self.click(OrderPageLocators.METRO_OPTION(metro_station))
            self.send_keys(OrderPageLocators.PHONE, phone)

    def fill_rent_data_form(self, date, rental_period, color, comment, *args, **kwargs):
        with allure.step(f"Заполнение данных аренды: дата={date}, срок={rental_period}, цвет={color}, комментарий={comment}"):
            day, month, year = date.split(".")
            self.click(OrderPageLocators.DATE_INPUT)
            self.click(OrderPageLocators.DATE_OPTION(day.lstrip('0')))
            self.click(OrderPageLocators.RENTAL_DROPDOWN)
            self.click(OrderPageLocators.RENTAL_OPTION(rental_period))
            self.click(OrderPageLocators.COLOR(color))
            self.send_keys(OrderPageLocators.COMMENT, comment)

    def create_order(self):
        with allure.step("Нажатие кнопки 'Заказать' на форме"):
            self.click(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        with allure.step("Подтверждение заказа во всплывающем окне"):
            self.click(OrderPageLocators.CONFIRM_BUTTON)

    def go_to_rent_data_form(self):
        with allure.step("Переход к форме данных аренды (кнопка 'Далее')"):
            self.click(OrderPageLocators.NEXT_BUTTON)

    def is_order_successful(self):
        with allure.step("Проверка успешного оформления заказа"):
            try:
                self.wait.until(expected_conditions.visibility_of_element_located(OrderPageLocators.SUCCESS_MODAL))
                return True
            except:
                return False
