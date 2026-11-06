from typing import Optional

from pydantic import BaseModel


class KeggNetwork(BaseModel):
    kegg_hsa: Optional[str] = None
    network_id: Optional[str] = None
    network_name: Optional[str] = None