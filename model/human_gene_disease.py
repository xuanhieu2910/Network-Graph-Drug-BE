from typing import Optional
from pydantic import BaseModel


class HumanGenDisease(BaseModel):
    hsa: Optional[str] = None
    association_type: Optional[str] = None
    mondo_id: Optional[str] = None    