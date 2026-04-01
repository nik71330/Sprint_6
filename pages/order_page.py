import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def fill_personal_data_form(self, first_name, last_name, address, metro_station, phone):
        with allure.step("Заполнение личных данных"):
            self.send_keys(OrderPageLocators.FIRST_NAME, first_name)
            self.send_keys(OrderPageLocators.LAST_NAME, last_name)
            self.send_keys(OrderPageLocators.ADDRESS, address)
            self.click(OrderPageLocators.METRO_STATION)
            self.click(OrderPageLocators.METRO_OPTION(metro_station))
            self.send_keys(OrderPageLocators.PHONE, phone)

    def fill_rent_data_form(self, date, rental_period, color, comment):
        with allure.step("Заполнение данных аренды"):
            day = date.split(".")[0].lstrip("0")

            self.click(OrderPageLocators.DATE_INPUT)
            self.click(OrderPageLocators.DATE_OPTION(day))

            self.click(OrderPageLocators.RENTAL_DROPDOWN)
            self.click(OrderPageLocators.RENTAL_OPTION(rental_period))
            self.click(OrderPageLocators.COLOR(color))
            self.send_keys(OrderPageLocators.COMMENT, comment)

    def go_to_rent_data_form(self):
        with allure.step("Переход к форме аренды"):
            self.click(OrderPageLocators.NEXT_BUTTON)

    def create_order(self):
        with allure.step("Нажатие кнопки 'Заказать'"):
            self.click(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        with allure.step("Подтверждение заказа"):
            self.wait_for_clickable(OrderPageLocators.CONFIRM_BUTTON)
            self.click(OrderPageLocators.CONFIRM_BUTTON)

    def is_order_successful(self):
        with allure.step("Проверка успешного заказа"):
            return self.wait_for_visible(OrderPageLocators.SUCCESS_MODAL).is_displayed()