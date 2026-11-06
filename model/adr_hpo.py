from typing import Optional

from pydantic import BaseModel

class AdrHpo(BaseModel):
    adr_umls_cui: Optional[str] = None
    hpo_id: Optional[str] = None
