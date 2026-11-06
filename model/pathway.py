from typing import Optional

from pydantic import BaseModel

class Pathway(BaseModel):
    pathway_id: Optional[str] = None
    pathway_name: Optional[str] = None
