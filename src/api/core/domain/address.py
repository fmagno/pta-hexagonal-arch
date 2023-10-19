from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class Address:
    id: UUID
    street_address: str
    city: str
    zip_code: str
    country: str
