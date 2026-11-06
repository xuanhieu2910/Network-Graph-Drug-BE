from repository.base_repository import BaseRepository
from model.kegg_disease import KeggDisease


class KeggDiseaseRepository(BaseRepository[KeggDisease]):

    def __init__(self, connection):
        super().__init__(connection, KeggDisease)

    def get_by_id(self, id:str):
        pass

    def get_by_code_hsa_and_id_diease(self, hsa_code: str, id_diease: str) -> KeggDisease:
        sql = """
                select * from kegg_disease WHERE kegg_hsa = %(hsa_code)s and %(disease_id)s
            """
        return self._query_one(
            sql,
            {
                'hsa_code': hsa_code,
                'disease_id' : id_diease
            }
        )

    def get_all(self) -> list[KeggDisease]:
        sql = " select * from kegg_disease"
        return self._query_all(sql)

    def create(self, obj : KeggDisease) -> KeggDisease:
        sql = """
            INSERT
            INTO kegg_disease (kegg_hsa, disease_id, disease_name)
            VALUES ( %(kegg_hsa)s, 
                    %(disease_id)s, 
                    %(disease_name)s )
            """
        return self._execute(sql, obj.model_dump())

    def delete(self, id: str):
        pass