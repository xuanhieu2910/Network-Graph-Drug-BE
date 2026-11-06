from typing import Optional

from pydantic import BaseModel

class KeggGene(BaseModel):

    kegg_hsa: Optional[str] = None
    kegg_entry: Optional[str] = None
    kegg_symbol: Optional[str] = None
    kegg_name: Optional[str] = None
    kegg_orthology: Optional[str] = None
    kegg_organism: Optional[str] = None