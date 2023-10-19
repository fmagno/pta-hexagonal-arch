from fastapi import APIRouter

from .first_order.routes import first_order_router

router = APIRouter()
router.include_router(router=first_order_router, prefix="/first-order", tags=["first-order"])  # noqa: E501
