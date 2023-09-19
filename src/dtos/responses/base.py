from pydantic import BaseModel


class BaseResponse(BaseModel):
    ...


class MessageResponse(BaseResponse):
    message: str


class VersionResponse(BaseResponse):
    version: str
