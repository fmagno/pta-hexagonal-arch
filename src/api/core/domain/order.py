from dataclasses import asdict, dataclass
from uuid import UUID

from api.core.domain.customer import CustomerCreate


# entities
@dataclass(slots=True)
class Order:
    id: UUID
    customer_id: UUID
    # basket_id: UUID
    # purchase_id: UUID
    # shipping_id: UUID

    to_dict = asdict


# value objects
@dataclass(slots=True)
class OrderCreate:
    customer_id: UUID
    # pizza: str


@dataclass(slots=True)
class FirstOrderCreate:
    customer: CustomerCreate

    @classmethod
    def from_dict(cls, first_order: dict):
        customer_dict = first_order.get("customer", {})
        customer: CustomerCreate = CustomerCreate.from_dict(customer=customer_dict)
        return cls(customer=customer)
