from repository.kegg_element_repository import KeggElementRepository    
from model.kegg_element import KeggElement

class KeggElementService():
    def __init__(self, connection):
        self.connection = connection
        self.repository = KeggElementRepository(connection)

    def find_all(self) -> list[KeggElement]:
        return self.repository.get_all()


    def find_by_hsa_code_and_element_id(self, hsa_code, element_id) -> KeggElement:
        return self.repository.get_by_hsa_code_and_element_id(hsa_code, element_id)

    

