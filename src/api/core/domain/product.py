from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class Product:
    id: UUID
    name: str
