from repository.unit_protein_kegg_gene_repository import UnitProteinKeggGeneRepository
from model.unit_protein_kegg_gene import UnitProteinKeggGene


class UnitProteinKeggGeneService():


    def __init__(self, connection):
        self.connection = connection
        self.unit_protein_kegg_gene_repository = UnitProteinKeggGeneRepository(self.connection)


    def create(self, obj: UnitProteinKeggGene) -> UnitProteinKeggGene:
        return self.unit_protein_kegg_gene_repository.create(obj)

    def get_by_code(self, protein_code: str) -> UnitProteinKeggGene:
        return self.unit_protein_kegg_gene_repository.get_by_id(protein_code)

    def find_all(self) -> list[UnitProteinKeggGene]:
        return self.unit_protein_kegg_gene_repository.get_all()

    def delete(self, protein_code: str) -> UnitProteinKeggGene:
        self.unit_protein_kegg_gene_repository.delete(protein_code)


    