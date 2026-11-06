from typing import List

from model.drug_adr_llt import DrugAdrLlt
from repository.drug_adr_repository import DrugAdrRepository

class DrugAdrService():
    def __init__(self, connection):
        self.connection = connection
        self.drug_adr_repository = DrugAdrRepository(connection=connection)


    def find_all(self) -> List[DrugAdrLlt]:
        return self.drug_adr_repository.get_all()
    