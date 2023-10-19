from fastapi import APIRouter, Depends, status
from api.controller.exceptions.schemas import (
    HTTP400BadRequestContent,
    HTTP500InternalServerErrorContent,
    HTTP500InternalServerErrorException,
    HTTP500InternalServerErrorResponse,
)
from api.controller.first_order.dtos import FirstOrderCreateDto, OrderReadDto
from api.core.domain.order import FirstOrderCreate, Order

from api.core.ports.outbound.logger import Logger, get_logger
from api.core.services.create_first_order import (
    CreateFirstOrderError,
    CreateFirstOrderSvc,
    get_create_first_order_svc,
)


first_order_router = APIRouter()


@first_order_router.post(
    "",
    response_model=OrderReadDto,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "model": HTTP400BadRequestContent,
            "description": "Bad request",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": HTTP500InternalServerErrorContent,
            "description": "Internal server error",
        },
    },
)
async def create_first_order(
    *,
    logger: Logger = Depends(get_logger),
    create_first_order_svc: CreateFirstOrderSvc = Depends(get_create_first_order_svc),
    first_order: FirstOrderCreateDto,
) -> OrderReadDto:
    """Create a first order."""

    await logger.info("controller handle: creating first order...", __name__)
    try:
        order: Order = await create_first_order_svc.handle(
            first_order=FirstOrderCreate.from_dict(
                first_order=first_order.model_dump(),
            ),
        )
    except CreateFirstOrderError:
        raise HTTP500InternalServerErrorException(
            response=HTTP500InternalServerErrorResponse(
                content=HTTP500InternalServerErrorContent(
                    code="500",
                    msg="Error creating first order",
                ),
            ),
        )
    else:
        order_read: OrderReadDto = OrderReadDto(**order.to_dict())

    return order_read
