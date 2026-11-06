from dataclasses import dataclass


@dataclass
class DrugProtein():

    type: str
    drugbank_id: str
    name: str
    description: str
    state: str
    groups: str
    protein_id: str