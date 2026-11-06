from typing import Optional

from pydantic import BaseModel

class DrugProtein(BaseModel):
    unit_protein_id: Optional[str] = None
    drug_bank_id: Optional[str] = None
    