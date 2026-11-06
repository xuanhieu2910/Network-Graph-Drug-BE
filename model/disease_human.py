from typing import Optional

from pydantic import BaseModel

class DiseaseHuman(BaseModel):
    mondo_id: Optional[str] = None
    disease_name: Optional[str] = None