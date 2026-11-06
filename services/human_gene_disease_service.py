from repository.human_gene_disease_repository import HumanGeneDiseaseRepository
from model.human_gene_disease import HumanGenDisease
class HumanGeneDiseaseService():
    def __init__(self, connection):
        self.connection = connection
        self.repository = HumanGeneDiseaseRepository(connection)


    def create(self, obj: HumanGenDisease) -> HumanGenDisease:
        return self.repository.create(obj)


    def find_by_id_hsa_and_mondo_id(self, 
                                    hsa_code: str, 
                                    mondo_code: str) -> HumanGenDisease:
        return self.repository.get_by_id_hsa_and_mondo(hsa_code,mondo_code)

    def delete_by_id_hsa_and_mondo_id(self, 
                                      hsa_code: str,
                                      mondo_code: str) -> None:
        self.repository.delete(hsa_code, mondo_code)

    def find_all(self) -> list[HumanGenDisease]:
        return self.repository.get_all()