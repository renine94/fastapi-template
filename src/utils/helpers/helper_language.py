from langdetect import detect


class LanguageHelper:
    @staticmethod
    def get_lang_code_from_str(text: str):
        return detect(text)
