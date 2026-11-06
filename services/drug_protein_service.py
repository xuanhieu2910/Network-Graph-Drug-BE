from repository.drug_protein_repository import DrugProteinRepository
from model.drug_protein import DrugProtein

class DrugProteinService():
    def __init__(self, connection):
        self.connection = connection
        self.repository = DrugProteinRepository(connection)

    def create(self, obj: DrugProtein) -> DrugProtein:
        return self.repository.create(obj)

    def find_by_id_drug_and_protein(self,
                                drug_code: str,
                                protein_code: str) -> DrugProtein:
        return self.repository.get_by_id_drug_and_protein(drug_code, protein_code)

    def delete(self, external_id: str) -> None:
        self.repository.delete(external_id)

    def find_all(self) -> list[DrugProtein]:
        return self.repository.get_all()
    