from typing import Optional

from pydantic import BaseModel

class KeggInformation(BaseModel):
    hsa: Optional[str] = None
    entry: Optional[str] = None
    symbol: Optional[str] = None
    name: Optional[str] = None
    orthology: Optional[str] = None
    organism: Optional[str] = None
    