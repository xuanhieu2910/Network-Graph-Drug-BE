from repository.proteins_repository import ProteinRepository
from model.proteins import Protein


class ProteinService():


    def __init__(self, connection):
        self.connection = connection
        self.protein_repository = ProteinRepository(self.connection)


    def create(self, obj: Protein) -> Protein:
        return self.protein_repository.create(obj)

    def get_by_code(self, protein_code: str) -> Protein:
        return self.protein_repository.get_by_id(protein_code)

    def find_all(self) -> list[Protein]:
        return self.protein_repository.get_all()

    def delete(self, protein_code: str) -> Protein:
        self.protein_repository.delete(protein_code)


    