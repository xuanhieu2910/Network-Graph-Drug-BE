from repository.kegg_gene_repository import KeggGeneRepository    
from model.kegg_gene import KeggGene

class KeggGeneService():


    def __init__(self, connection):
        self.connection = connection
        self.repository = KeggGeneRepository(connection)

    def find_all(self) -> list[KeggGene]:
        return self.repository.get_all()


    def find_by_hsa_code(self, hsa_code) -> KeggGene:
        return self.repository.get_by_id(hsa_code)

    

