from repository.kegg_disease_repository import KeggDiseaseRepository
from model.kegg_disease import KeggDisease


class KeggDiseaseService():

    def __init__(self, connection):
        self.connection = connection
        self.repository = KeggDiseaseRepository(connection)

    def create(self, obj: KeggDisease) -> KeggDisease:
        return self.repository.create(obj)

    def find_by_hsa_code_and_diease_id(self, hsa_code:str, diease_id:str) -> KeggDisease:
        return self.repository.get_by_code_hsa_and_id_diease(hsa_code, diease_id)

    def find_all(self) -> list[KeggDisease]:
        return self.repository.get_all()