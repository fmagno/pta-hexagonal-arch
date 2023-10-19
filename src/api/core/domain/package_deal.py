import datetime
from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class PackageDeal:
    id: UUID
    name: str
    products_ids: list[UUID]
    price: float
    valid_from: datetime.datetime
    valid_until: datetime.datetime
