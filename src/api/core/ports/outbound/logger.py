from abc import ABC
from fastapi import Depends
from api.settings.factory import get_settings

from api.settings.pydantic import Settings


class Logger(ABC):
    def __init__(self, settings: Settings):
        self.settings = settings

    async def info(self, message: object, module_name: str):
        raise NotImplementedError()

    async def debug(self, message: object, module_name: str):
        raise NotImplementedError()

    async def warn(self, message: object, module_name: str):
        raise NotImplementedError()

    async def error(self, message: object, module_name: str):
        raise NotImplementedError()


# factories
async def logger_factory(settings: Settings) -> Logger:
    logger = Logger(settings=settings)
    return logger


# dependencies
async def get_logger(settings: Settings = Depends(get_settings)) -> Logger:
    logger = await logger_factory(settings=settings)
    return logger
