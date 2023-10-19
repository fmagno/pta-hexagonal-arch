import logging
import logging.config
from api.settings.pydantic import Settings
from api.core.ports.outbound.logger import Logger
from fastapi import Depends
from api.settings.factory import get_settings


class DevLogger(Logger):
    def __init__(self, settings: Settings):
        logging.basicConfig(
            format="%(asctime)s - %(module_name)s - %(levelname)s - %(message)s",
            level=logging.DEBUG,
        )
        self.logger = logging.getLogger(__name__)

    async def info(self, message: object, module_name: str):
        self.logger.info(message, extra={"module_name": module_name})

    async def debug(self, message: object, module_name: str):
        self.logger.debug(message, extra={"module_name": module_name})

    async def warn(self, message: object, module_name: str):
        self.logger.warn(message, extra={"module_name": module_name})

    async def error(self, message: object, module_name: str):
        self.logger.error(message, extra={"module_name": module_name})


# factories
async def logger_dev_factory(settings: Settings) -> Logger:
    logger = DevLogger(settings=settings)
    return logger


# dependencies
async def get_logger_dev(settings: Settings = Depends(get_settings)) -> Logger:
    logger = await logger_dev_factory(settings=settings)
    return logger
