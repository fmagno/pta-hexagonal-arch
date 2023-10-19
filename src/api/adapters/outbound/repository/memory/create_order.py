import uuid
from fastapi import Depends
from api.core.domain.order import OrderCreate, Order
from api.core.ports.outbound.logger import Logger, get_logger
from api.core.ports.outbound.repository.create_order import (
    CreateOrderRepository,
)
from api.settings.factory import get_settings
from api.settings.pydantic import Settings


class CreateOrderRepositoryMemory(CreateOrderRepository):
    def __init__(
        self,
        settings: Settings,
        logger: Logger,
    ):
        super().__init__(
            settings=settings,
            logger=logger,
        )

    async def handle(
        self,
        order: OrderCreate,
    ) -> Order:
        new_order = Order(id=uuid.uuid4(), customer_id=order.customer_id)
        # raise Exception("Boom! Failed new order...")
        await self.logger.info(f"New order stored... {new_order}", __name__)
        return new_order


# factories
async def create_order_repo_memory_fct(
    settings: Settings,
    logger: Logger,
) -> CreateOrderRepositoryMemory:
    create_order_repo_memory = CreateOrderRepositoryMemory(
        settings=settings,
        logger=logger,
    )
    return create_order_repo_memory


# dependencies
async def get_create_order_repo_memory(
    settings: Settings = Depends(get_settings),
    logger: Logger = Depends(get_logger),
) -> CreateOrderRepositoryMemory:
    create_order_repo_memory = await create_order_repo_memory_fct(
        settings=settings,
        logger=logger,
    )
    return create_order_repo_memory
