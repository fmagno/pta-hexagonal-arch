from dataclasses import dataclass
from uuid import UUID


# entities
@dataclass(slots=True)
class Customer:
    id: UUID
    name: str


# value objects
@dataclass(slots=False)
class CustomerCreate:
    name: str

    @classmethod
    def from_dict(cls, customer: dict) -> "CustomerCreate":
        name_dict = customer.get("name", {})
        name = name_dict
        return cls(name=name)
