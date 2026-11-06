from typing import Optional
from pydantic import BaseModel

class HumanPhenotypeOntology(BaseModel):
    hpo_id: Optional[str] = None
    hpo_name: Optional[str] = None

    