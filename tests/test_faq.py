import pytest
from test_data.faq_data import FAQ_DATA


class TestFAQ:

    @pytest.mark.parametrize("question_text, expected_text", FAQ_DATA)
    def test_faq_question_opens_correct_answer(self, home_page, question_text, expected_text):
        home_page.open()
        home_page.click_question_by_text(question_text)
        actual_text = home_page.get_answer_text_by_text(question_text, expected_text)
        assert actual_text == expected_text