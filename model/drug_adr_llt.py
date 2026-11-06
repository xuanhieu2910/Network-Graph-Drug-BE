from typing import Optional

from pydantic import BaseModel

class DrugAdrLlt(BaseModel):
    drug_bank_id: Optional[str] = None
    adr_umls_cui: Optional[str] = None
    source: Optional[str] = None
    