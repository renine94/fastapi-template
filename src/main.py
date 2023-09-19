from fastapi import FastAPI

from src.core import settings
from src.core.exceptions import CustomException
from src.core.exceptions import custom_exception_handler
from src.routers import router


class MyFastAPI(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # routers
        self.include_router(router)
        # exceptions
        self.add_exception_handler(CustomException, custom_exception_handler)


app = MyFastAPI(
    title="Quizium-Backend for B2B",
    debug=settings.DEBUG,
    description="This API Server is aim to serving api for B2B",
    version=settings.VERSION,
)
