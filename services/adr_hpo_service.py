from repository.adr_hpo_repository import AdrHpoRepository
from model.adr_hpo import AdrHpo




class AdrHpoService():

    def __init__(self, connection):
        self.connection = connection
        self.repository = AdrHpoRepository(connection)

    def create(self, obj: AdrHpo) -> AdrHpo:
        return self.repository.create(obj)

    def find_by_adr_umls_cui(self, adr_umls_cui: str) -> AdrHpo:
        return self.repository.get_by_id(adr_umls_cui=adr_umls_cui)

    def delete(self, adr_umls_cui: str) -> None:
        self.repository.delete(adr_umls_cui=adr_umls_cui)

    def find_all(self) -> list[AdrHpo]:
        return self.repository.get_all()