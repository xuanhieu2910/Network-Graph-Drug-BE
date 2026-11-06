from dataclasses import dataclass


@dataclass
class Drug():
    sid: str
    data_source: str
    external_id: str
    synonyms: str
    data_source_category: str
    compound_cid: str
    last_modified_date: str
    deposit_date: str
    name: str
    smiles: str
