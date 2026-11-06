from typing import List

from repository.adr_llt_repository import AdrLltRepository
from model.drugs_smiles import DrugsSmiles

class AdrLltService():
    def __init__(self, connection):
        self.connection = connection
        self.adr_llt_repository = AdrLltRepository(connection=connection)


    def find_all(self) -> List[DrugsSmiles]:
        return self.adr_llt_repository.get_all()
    