from typing import Optional
from pydantic import BaseModel

class UnitProteinKeggGene(BaseModel):
    uniprot_id: Optional[str] = None
    kegg_gene: Optional[str] = None