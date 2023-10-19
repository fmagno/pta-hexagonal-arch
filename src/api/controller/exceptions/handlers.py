from fastapi import Request, status
from fastapi.responses import JSONResponse

from api.controller.exceptions.schemas import HTTP400BadRequestException


async def http_400_bad_request_exception_handler(
    request: Request,
    exc: HTTP400BadRequestException,
):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=exc.response.content.model_dump(),
        headers=exc.response.headers,
    )
