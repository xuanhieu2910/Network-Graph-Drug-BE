from typing import Optional
from pydantic import BaseModel

class MondoHumanPhenotype(BaseModel):
    mondo_id: Optional[str] = None
    database_id: Optional[str] = None
    hpo_id: Optional[str] = None
    frequency: Optional[str] = None