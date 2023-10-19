from abc import ABC

from fastapi import Depends

from api.core.domain.customer import CustomerCreate
from api.core.ports.outbound.logger import Logger, get_logger
from api.settings.factory import get_settings
from api.settings.pydantic import Settings


class CreateCustomerRepository(ABC):
    def __init__(
        self,
        settings: Settings,
        logger: Logger,
    ):
        self.settings = settings
        self.logger = logger

    async def handle(
        self,
        customer: CustomerCreate,
    ):
        raise NotImplementedError("CreateCustomerRepository handle missing.")


# factories
async def create_customer_repo_factory(
    settings: Settings,
    logger: Logger,
) -> CreateCustomerRepository:
    create_customer_repo = CreateCustomerRepository(
        settings=settings,
        logger=logger,
    )
    return create_customer_repo


# dependencies
async def get_create_customer_repo(
    settings: Settings = Depends(get_settings),
    logger: Logger = Depends(get_logger),
) -> CreateCustomerRepository:
    create_customer_repo = await create_customer_repo_factory(
        settings=settings,
        logger=logger,
    )
    return create_customer_repo
