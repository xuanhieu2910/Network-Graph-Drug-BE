from typing import Optional

from pydantic import BaseModel

class Protein(BaseModel):
    name: Optional[str] = None
    unit_protein_id: Optional[str] = None
    