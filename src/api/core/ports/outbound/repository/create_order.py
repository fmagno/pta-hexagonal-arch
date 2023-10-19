from abc import ABC

from fastapi import Depends

from api.core.domain.order import OrderCreate
from api.core.ports.outbound.logger import Logger, get_logger
from api.settings.factory import get_settings
from api.settings.pydantic import Settings


class CreateOrderRepository(ABC):
    def __init__(
        self,
        settings: Settings,
        logger: Logger,
    ):
        self.settings = settings
        self.logger = logger

    async def handle(
        self,
        order: OrderCreate,
    ):
        raise NotImplementedError("CreateOrderRepository handle missing.")


# factories
async def create_order_repo_factory(
    settings: Settings,
    logger: Logger,
) -> CreateOrderRepository:
    create_order_repo = CreateOrderRepository(
        settings=settings,
        logger=logger,
    )
    return create_order_repo


# dependencies
async def get_create_order_repo(
    settings: Settings = Depends(get_settings),
    logger: Logger = Depends(get_logger),
) -> CreateOrderRepository:
    create_order_repo = await create_order_repo_factory(
        settings=settings,
        logger=logger,
    )
    return create_order_repo
