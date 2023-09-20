import ast
import json
from json import JSONDecodeError

import openai
import tiktoken
from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import select_autoescape
from openai import OpenAIError

from src.core import settings


class OpenAI:
    openai.organization = None
    openai.api_key = settings.API_KEY_AZURE_OPENAI
    openai.api_type = "azure"
    openai.api_base = "https://eastus.api.cognitive.microsoft.com/"
    openai.api_version = "2023-03-15-preview"

    @classmethod
    async def aget_response(cls, prompt: str) -> dict | None:
        try:
            engine = cls.get_engine(prompt)
            messages = [{"role": "user", "content": prompt}]
            response = await openai.ChatCompletion.acreate(engine=engine, messages=messages)
        except OpenAIError as e:
            print(e)
            return None

        result = {}
        response_dict = response.to_dict()
        result["model_type"] = response_dict["model"]
        result["use_token"] = response_dict["usage"].to_dict()
        try:
            result["data"] = json.loads(response_dict["choices"][0]["message"]["content"])
        except JSONDecodeError:
            try:
                result["data"] = ast.literal_eval(response_dict["choices"][0]["message"]["content"])
            except Exception:
                return None
        return result

    @classmethod
    def get_token_size(cls, prompt: str) -> int:
        gpt35_encoder = tiktoken.encoding_for_model("gpt-3.5-turbo")
        tokens = gpt35_encoder.encode(prompt)
        return len(tokens)

    @classmethod
    def get_engine(cls, prompt: str) -> str:
        token_length = cls.get_token_size(prompt)

        if settings.ENV in ["local", "dev"]:
            return "cog-gpt35-turbo-16k-dev" if token_length >= 3200 else "cog-gpt35-turbo-dev"
        return "cog-gpt35-turbo-16k-prod" if token_length >= 3200 else "cog-gpt35-turbo-prod"

    @classmethod
    def get_prompt(cls, name: str, **kwargs):
        """
        :param name: this is assets/prompts/filename, ex) mcq.jinja2
        :param kwargs: check the prompt file content
        """
        env = Environment(
            loader=FileSystemLoader(f"{settings.BASE_DIR}/assets/prompts/"),
            autoescape=select_autoescape(),
        )
        template = env.get_template(name)
        prompt = template.render(**kwargs)
        return prompt
