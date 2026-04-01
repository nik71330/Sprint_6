import allure
from test_data.order_data import ORDER_USERS


class TestOrder:

    @allure.epic("UI Тесты")
    @allure.feature("Заказ самоката")
    @allure.story("Позитивный сценарий: заказ через верхнюю кнопку")
    def test_positive_order_flow_top_button_user1(self, home_page, order_page):
        user = ORDER_USERS[0]

        with allure.step("Открываем главную страницу и жмем верхнюю кнопку 'Заказать'"):
            home_page.open()
            home_page.click_order_top()

        with allure.step("Заполняем форму личных данных"):
            order_page.fill_personal_data_form(
                first_name=user["first_name"],
                last_name=user["last_name"],
                address=user["address"],
                metro_station=user["metro_station"],
                phone=user["phone"],
            )

        with allure.step("Переходим к форме аренды и заполняем её"):
            order_page.go_to_rent_data_form()
            order_page.fill_rent_data_form(
                date=user["date"],
                rental_period=user["rental_period"],
                color=user["color"],
                comment=user["comment"],
            )

        with allure.step("Создаем и подтверждаем заказ"):
            order_page.create_order()
            order_page.confirm_order()

        assert order_page.is_order_successful()

    @allure.epic("UI Тесты")
    @allure.feature("Заказ самоката")
    @allure.story("Позитивный сценарий: заказ через нижнюю кнопку")
    def test_positive_order_flow_bottom_button_user1(self, home_page, order_page):
        user = ORDER_USERS[1]

        with allure.step("Открываем главную страницу и жмем нижнюю кнопку 'Заказать'"):
            home_page.open()
            home_page.click_order_bottom()

        with allure.step("Заполняем форму личных данных"):
            order_page.fill_personal_data_form(
                first_name=user["first_name"],
                last_name=user["last_name"],
                address=user["address"],
                metro_station=user["metro_station"],
                phone=user["phone"],
            )

        with allure.step("Переходим к форме аренды и заполняем её"):
            order_page.go_to_rent_data_form()
            order_page.fill_rent_data_form(
                date=user["date"],
                rental_period=user["rental_period"],
                color=user["color"],
                comment=user["comment"],
            )

        with allure.step("Создаем и подтверждаем заказ"):
            order_page.create_order()
            order_page.confirm_order()

        assert order_page.is_order_successful()