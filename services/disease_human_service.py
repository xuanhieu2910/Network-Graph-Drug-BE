from repository.disease_human_repository import DiseaseHumanRepository
from model.disease_human import DiseaseHuman



class DiseaseHumanService():

    def __init__(self, connection):
        self.connection = connection
        self.repository = DiseaseHumanRepository(connection)

    def create(self, obj: DiseaseHuman) -> DiseaseHuman:
        return self.repository.create(obj)

    def find_by_mondo_id(self, mondo_code: str) -> DiseaseHuman:
        return self.repository.get_by_id(mondo_id=mondo_code)

    def delete(self, mondo_code: str) -> None:
        self.repository.delete(mondo_id= mondo_code)

    def find_all(self) -> list[DiseaseHuman]:
        return self.repository.get_all()