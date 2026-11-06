from repository.base_repository import BaseRepository
from model.kegg_element import KeggElement


class KeggElementRepository(BaseRepository[KeggElement]):


    def __init__(self, connection):
        super().__init__(connection, KeggElement)

    def get_by_id(self, id:str):
        pass

    def get_by_hsa_code_and_element_id(self, hsa_code: str, element_id: str) -> KeggElement:
        sql = """
            SELECT * FROM kegg_element WHERE kegg_hsa = %(kegg_hsa)s and element_id = %(element_id)s
        """
        return self._query_one(
            sql,
            {
                "kegg_hsa" : hsa_code,
                "element_id" : element_id
            }
        )

    def get_all(self) -> list[KeggElement]:
        sql = "SELECT * FROM kegg_element LIMIT 200"
        return self._query_all(sql)

    def crate(self, obj: KeggElement) -> KeggElement:
        pass

    def delete(self, id: str):
        pass
