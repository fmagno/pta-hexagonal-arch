from typing import Protocol

from api.core.domain.order import OrderCreate


class OrderRepository(Protocol):
    def create(self, order: OrderCreate):
        raise NotImplementedError()
