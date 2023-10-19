from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class Basket:
    id: UUID
    package_deals_ids: list[UUID]
