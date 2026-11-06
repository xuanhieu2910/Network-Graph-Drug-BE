from typing import Optional

from pydantic import BaseModel

class AdrLlt(BaseModel):
    adr_umls_cui: Optional[str] = None
    adr_name: Optional[str] = None
    meddra_level: Optional[str] = None
    