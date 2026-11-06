from repository.kegg_pathway_repository import KeggPathwayRepository
from model.kegg_pathway import KeggPathway


class KeggPathwayService():
    def __init__(self, connection):
        self.connection = connection
        self.repository = KeggPathwayRepository(connection)

    def find_all(self) -> list[KeggPathway]:
        return self.repository.get_all()

    def find_by_hsa_code_and_pathway_id(self, hsa_code: str, pathway_id: str) -> KeggPathway:
        return self.repository.get_by_hsa_code_and_pathway_id(hsa_code, pathway_id)