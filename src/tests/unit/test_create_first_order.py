import pytest
from api.core.domain.customer import CustomerCreate
from api.core.domain.order import FirstOrderCreate, Order
from api.core.services.create_customer import create_customer_fct

from api.core.services.create_first_order import (
    CreateFirstOrderSvc,
    create_first_order_fct,
)


pytestmark = pytest.mark.asyncio


@pytest.fixture
async def create_customer_svc(
    logger_dev,
    create_customer_repo_memory,
):
    create_customer_svc = await create_customer_fct(
        logger=logger_dev,
        create_customer_repo=create_customer_repo_memory,
    )
    return create_customer_svc


@pytest.fixture
async def create_first_order_svc(
    logger_dev,
    create_customer_svc,
    create_first_order_repo_memory,
) -> CreateFirstOrderSvc:
    create_first_order_svc: CreateFirstOrderSvc = await create_first_order_fct(
        logger=logger_dev,
        create_customer_svc=create_customer_svc,
        create_first_order_repo=create_first_order_repo_memory,
    )
    return create_first_order_svc


@pytest.mark.unit
@pytest.mark.first_order
async def test_first_order_creation_with_valid_payload(
    create_first_order_svc,
) -> None:
    """
    Unit: Should create a first order successfully with a valid payload.
    """

    order: Order = await create_first_order_svc.handle(
        first_order=FirstOrderCreate(
            customer=CustomerCreate(name="Jane"),
        ),
    )
    assert order.id is not None


# def test_create_first_order(settings):
