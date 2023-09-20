from src.utils.helpers.helper_language import LanguageHelper


def test_get_lang_code_from_str_success():
    # Given
    expected_lang_code = "ko"
    text = "안녕하세요."

    # When
    result = LanguageHelper.get_lang_code_from_str(text)

    # Then
    assert expected_lang_code == result
