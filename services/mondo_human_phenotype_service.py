from model.mondo_human_phenotype import MondoHumanPhenotype
from repository.mondo_human_phenotype_repository import MondoHumanPhenotypeRepository


class MondoHumanPhenotypeService():
    def __init__(self, connection):
        self.connection = connection
        self.repository = MondoHumanPhenotypeRepository(connection)

    def find_all(self) -> list[MondoHumanPhenotype]:
        return self.repository.get_all()

    def find_by_id(self, id: str) -> MondoHumanPhenotype:
        return self.repository.get_by_id(id)