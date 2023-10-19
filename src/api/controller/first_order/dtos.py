import uuid
from pydantic import BaseModel


class FirstOrderAddress(BaseModel):
    name: str
    street_no: str
    city: str
    state: str
    postal_code: str
    country: str


class FirstOrderCustomer(BaseModel):
    name: str
    # first_name: str
    # last_name: str


class Product(BaseModel):
    name: str
    ref_code: str


class Basket(BaseModel):
    products: list[Product]


class Purchase(BaseModel):
    ...


class Shipping(BaseModel):
    ...


class FirstOrderCreateDto(BaseModel):
    customer: FirstOrderCustomer
    # basket: Basket
    # purchase: Purchase
    # shipping: Shipping


class OrderReadDto(BaseModel):
    id: uuid.UUID
    customer_id: uuid.UUID
