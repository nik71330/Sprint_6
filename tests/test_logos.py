import allure


class TestLogos:

    def test_clicking_samokat_logo_redirects_to_home_page(self, home_page):
        home_page.open()
        home_page.click_order_top()
        home_page.click_samokat_logo()
        assert home_page.is_on_main_page()

    def test_clicking_yandex_logo_opens_dzen_in_new_tab(self, home_page):
        home_page.open()
        home_page.click_yandex_logo()

        assert home_page.switch_to_new_window()
        assert "dzen.ru" in home_page.get_current_url().lower()