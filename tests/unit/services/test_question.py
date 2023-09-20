import pytest

from src.services.question import QuestionService


def test_split_script_success():
    # Given
    script = "1234567891011121314151617181920"
    count = 10

    # When
    splited_script = QuestionService.split_script(script, count)

    # Then
    assert isinstance(splited_script, list)
    assert len(splited_script) == count
    assert "".join(splited_script) == script


async def test_bulk_create_from_openai_success():
    # Given
    scripts = [
        "I'm strong man because I'm very tall and have a big hands",
        "I'm very pretty because i have a small face, big eyes",
    ]

    # When
    questions = await QuestionService.bulk_create_from_openai(scripts)

    # Then
    assert len(questions) == len(scripts)
