from dataclasses import dataclass


@dataclass
class Protein():

    source_name: str
    source_id: str
    description: str
    url: str
    code: str
    link_records: str