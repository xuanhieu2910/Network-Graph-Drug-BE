from typing import Optional
from pydantic import BaseModel

class KeggPathway(BaseModel):
    kegg_hsa: Optional[str] = None
    pathway_id: Optional[str] = None
    pathway_name: Optional[str] = None