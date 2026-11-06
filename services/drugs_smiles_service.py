from typing import List

from repository.drug_smiles_repository import DrugSmilesRepository
from model.drugs_smiles import DrugsSmiles

class DrugSmilesService():
    def __init__(self, connection):
        self.connection = connection
        self.drug_smiles_repository = DrugSmilesRepository(connection=connection)

    def find_by_id(self, external_id: str) -> DrugsSmiles:
        return self.drug_smiles_repository.get_by_id(external_id=external_id)


    def find_all(self) -> List[DrugsSmiles]:
        return self.drug_smiles_repository.get_all()
    