from typing import Dict, Union
from pydantic import BaseModel


class HTTP400BadRequestContent(BaseModel):
    code: str = "HTTP_400"
    msg: str = "Bad request"


class HTTP400BadRequestResponse(BaseModel):
    content: HTTP400BadRequestContent = HTTP400BadRequestContent()
    headers: Union[Dict[str, str], None] = None


class HTTP400BadRequestException(Exception):
    def __init__(
        self,
        response: HTTP400BadRequestResponse = HTTP400BadRequestResponse(),
    ):
        self.response = response


class HTTP500InternalServerErrorContent(BaseModel):
    code: str = "HTTP_500"
    msg: str = "Internal server error"


class HTTP500InternalServerErrorResponse(BaseModel):
    content: HTTP500InternalServerErrorContent = HTTP500InternalServerErrorContent()  # noqa: E501
    headers: Union[Dict[str, str], None] = None


class HTTP500InternalServerErrorException(Exception):
    def __init__(
        self,
        response: HTTP500InternalServerErrorResponse = HTTP500InternalServerErrorResponse(),  # noqa: E501
    ):
        self.response = response
