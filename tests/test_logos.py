import allure

class TestLogos:

    @allure.epic("UI Тесты")
    @allure.feature("Логотипы")
    @allure.story("Переход на главную страницу при клике на логотип 'Самокат'")
    def test_clicking_samokat_logo_redirects_to_home_page(self, home_page):
        with allure.step("Открываем страницу и кликаем по логотипу 'Самокат'"):
            home_page.open()
            home_page.click_order_top()
            home_page.click_samokat_logo()
            assert home_page.is_on_main_page()

    @allure.epic("UI Тесты")
    @allure.feature("Логотипы")
    @allure.story("Открытие Дзена при клике на логотип 'Яндекс'")
    def test_clicking_yandex_logo_opens_dzen_in_new_tab(self, home_page):
        with allure.step("Открываем страницу и кликаем по логотипу 'Яндекс'"):
            home_page.open()
            home_page.click_yandex_logo()
            assert home_page.switch_to_new_window()
            current_url = home_page.get_current_url().lower()
            assert "dzen.ru" in current_url
