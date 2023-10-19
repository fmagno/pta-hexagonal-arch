import datetime
from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class Purchase:
    id: UUID
    credit_card_no: str
    expiry_date: datetime.datetime
    cvv: str
    name: str
    date: datetime.datetime
