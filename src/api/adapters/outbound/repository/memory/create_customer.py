import uuid
from fastapi import Depends
from api.core.domain.customer import Customer, CustomerCreate
from api.core.ports.outbound.logger import Logger, get_logger
from api.core.ports.outbound.repository.create_customer import (
    CreateCustomerRepository,
)
from api.settings.factory import get_settings
from api.settings.pydantic import Settings


class CreateCustomerRepositoryMemory(CreateCustomerRepository):
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
        customer: CustomerCreate,
    ) -> Customer:
        new_customer = Customer(id=uuid.uuid4(), name=customer.name)
        await self.logger.info(f"New customer stored... {new_customer}", __name__)
        return new_customer


# factories
async def create_customer_repo_memory_fct(
    settings: Settings,
    logger: Logger,
) -> CreateCustomerRepositoryMemory:
    create_customer_repo_memory = CreateCustomerRepositoryMemory(
        settings=settings,
        logger=logger,
    )
    return create_customer_repo_memory


# dependencies
async def get_create_customer_repo_memory(
    settings: Settings = Depends(get_settings),
    logger: Logger = Depends(get_logger),
) -> CreateCustomerRepositoryMemory:
    create_customer_repo_memory = await create_customer_repo_memory_fct(
        settings=settings,
        logger=logger,
    )
    return create_customer_repo_memory
