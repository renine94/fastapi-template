from fastapi import Header

from src.core import settings
from src.core.exceptions import ValueException


async def get_api_key(api_key: str = Header(description="Please put in the issued key.")):
    if api_key != settings.API_KEY:
        raise ValueException("Invalid api_key.")
