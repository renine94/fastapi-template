import asyncio

from src.services.base import BaseService
from src.utils.helpers.helper_language import LanguageHelper
from src.utils.third_party.openai import OpenAI


class QuestionService(BaseService):
    @staticmethod
    def split_script(script: str, count: int) -> list[str]:
        """대본과 문제 생성 원하는 개수를 받아서 생성하고 리턴한다."""
        chunk_size = len(script) // count

        split_text_list = []
        for idx, size in enumerate(range(chunk_size, len(script) + 1, chunk_size)):
            text = script[chunk_size * idx : size]
            if idx + 1 == count:
                text = script[chunk_size * idx :]
            split_text_list.append(text)

        return split_text_list

    @staticmethod
    async def bulk_create_from_openai(scripts: list[str]) -> list[dict]:
        lang_code = LanguageHelper.get_lang_code_from_str("".join(scripts))

        tasks = []
        for script in scripts:
            prompt = OpenAI.get_prompt("mcq.jinja2", script=script, lang_code=lang_code)
            tasks.append(OpenAI.aget_response(prompt))

        responses = await asyncio.gather(*tasks)
        questions = [obj["data"] for obj in responses if obj]
        return questions
