from typing import Optional
from pydantic import BaseModel

class KeggDrugTarget(BaseModel):
    kegg_hsa: Optional[str] = None
    drug_target_id: Optional[str] = None
    drug_target_name: Optional[str] = None

    
