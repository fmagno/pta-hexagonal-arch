from fastapi import Depends
from api.core.domain.customer import Customer
from api.core.domain.order import FirstOrderCreate, Order, OrderCreate
from api.core.ports.outbound.logger import Logger, get_logger

from api.core.ports.outbound.repository.create_order import (
    CreateOrderRepository,
    get_create_order_repo,
)
from api.core.services.create_customer import (
    CreateCustomerSvc,
    get_create_customer_svc,
)


class CreateFirstOrderError(Exception):
    ...


class CreateFirstOrderSvc:
    def __init__(
        self,
        logger: Logger,
        create_customer_svc: CreateCustomerSvc,
        create_order_repo: CreateOrderRepository,
    ):
        self.logger = logger
        self.create_customer_svc = create_customer_svc
        self.create_order_repo = create_order_repo

    async def handle(
        self,
        first_order: FirstOrderCreate,
    ) -> Order:
        await self.logger.info("Creating a first order...", __name__)

        customer: Customer = await self.create_customer_svc.handle(
            customer=first_order.customer,
        )

        await self.logger.info(f"Customer created: {customer}", __name__)
        try:
            order: Order = await self.create_order_repo.handle(
                order=OrderCreate(customer_id=customer.id),
            )
        except Exception:
            await self.logger.error("Error during create_order_repo.handle", __name__)
            await self.logger.info("Undoing `create_first_order`", __name__)
            # TODO: remove customer by id
            raise CreateFirstOrderError
        else:
            return order


# factories
async def create_first_order_fct(
    logger: Logger,
    create_customer_svc: CreateCustomerSvc,
    create_first_order_repo: CreateOrderRepository,
):
    create_first_order_svc = CreateFirstOrderSvc(
        logger=logger,
        create_customer_svc=create_customer_svc,
        create_order_repo=create_first_order_repo,
    )
    return create_first_order_svc


# Dependencies
async def get_create_first_order_svc(
    logger: Logger = Depends(get_logger),
    create_customer_svc: CreateCustomerSvc = Depends(get_create_customer_svc),
    create_first_order_repo: CreateOrderRepository = Depends(
        get_create_order_repo,
    ),
) -> CreateFirstOrderSvc:
    create_first_order_svc = await create_first_order_fct(
        logger=logger,
        create_customer_svc=create_customer_svc,
        create_first_order_repo=create_first_order_repo,
    )
    return create_first_order_svc
