from typing import Optional
from pydantic import BaseModel
class DrugsSmiles(BaseModel):
    sid: Optional[int] = None
    data_source: Optional[str] = None
    external_id: Optional[str] = None
    synonyms: Optional[str] = None
    data_source_category: Optional[str] = None
    compound_cid: Optional[int] = None
    name: Optional[str] = None
    smiles: Optional[str] = None