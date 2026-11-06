from typing import Optional

from pydantic import BaseModel

class KeggDisease(BaseModel):
    kegg_hsa: Optional[str] = None
    disease_id: Optional[str] = None
    disease_name: Optional[str] = None
    