from typing import Optional

from pydantic import BaseModel

class KeggElement(BaseModel):
    kegg_hsa: Optional[str] = None
    element_id: Optional[str] = None
    element_name: Optional[str] = None
    