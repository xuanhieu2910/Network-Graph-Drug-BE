from repository.human_phenotype_ontology_repository import HumanPhenotypeOntologyRepository
from model.human_phenotype_ontology import HumanPhenotypeOntology


class HumanPhenotypeOntologyService():
    def __init__(self, connection):
        self.connection = connection
        self.repository = HumanPhenotypeOntologyRepository(connection)

    def find_all(self) -> list[HumanPhenotypeOntology]:
        return self.repository.get_all()

    def find_by_id_human_phenotype_ontology(self, human_phenotype_ontology_code: str) -> HumanPhenotypeOntology:
        return self.repository.get_by_id(human_phenotype_ontology_code)