import allure
import pytest

from test_data.faq_data import FAQ_DATA


@allure.epic("UI Тесты")
@allure.feature("FAQ")
@allure.story("Проверка раскрытия вопросов в разделе 'Вопросы о важном'")
class TestFAQ:

    @pytest.mark.parametrize("question_text, expected_text", FAQ_DATA)
    def test_faq_question_opens_correct_answer(self, home_page, question_text, expected_text):
        home_page.open()
        home_page.click_question_by_text(question_text)
        with allure.step(f"Открываем главную страницу и проверяем вопрос: {question_text}"):
            home_page.open()
            home_page.click_question_by_text(question_text)
            answer = home_page.get_answer_text_by_text(question_text, expected_text)
            assert expected_text in answer
