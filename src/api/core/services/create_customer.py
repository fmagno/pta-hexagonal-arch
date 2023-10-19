from fastapi import Depends
from api.core.domain.customer import Customer, CustomerCreate
from api.core.ports.outbound.logger import Logger, get_logger
from api.core.ports.outbound.repository.create_customer import (
    CreateCustomerRepository,
    get_create_customer_repo,
)


class CreateCustomerSvc:
    def __init__(
        self,
        logger: Logger,
        create_customer_repo: CreateCustomerRepository,
    ):
        self.logger = logger
        self.create_customer_repo = create_customer_repo

    async def handle(
        self,
        customer: CustomerCreate,
    ) -> Customer:
        await self.logger.info(f"Creating a customer... {customer}", __name__)

        new_customer: Customer = await self.create_customer_repo.handle(
            customer=customer,
        )

        return new_customer
        # return Customer(id=uuid.uuid4(), name="Jack")


# factories
async def create_customer_fct(
    logger: Logger,
    create_customer_repo: CreateCustomerRepository,
):
    create_customer_svc = CreateCustomerSvc(
        logger=logger,
        create_customer_repo=create_customer_repo,
    )
    return create_customer_svc


# Dependencies
async def get_create_customer_svc(
    logger: Logger = Depends(get_logger),
    create_customer_repo: CreateCustomerRepository = Depends(
        get_create_customer_repo,
    ),
) -> CreateCustomerSvc:
    create_customer_svc = await create_customer_fct(
        logger=logger,
        create_customer_repo=create_customer_repo,
    )
    return create_customer_svc
