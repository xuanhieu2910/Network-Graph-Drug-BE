from repository.base_repository import BaseRepository
from model.adr_llt import AdrLlt

class AdrLltRepository(BaseRepository[AdrLlt]):
    
    def __init__(self, connection):
        super().__init__(connection, AdrLlt)

    def get_by_id(self, external_id: str) -> AdrLlt:
        pass


    def get_all(self) -> list[AdrLlt]:
        sql = """
            SELECT adr_llt.* FROM adr_llt
            inner join (SELECT adr_umls_cui
            FROM drug_adr_llt
            WHERE drug_bank_id in ('DB01254','DB04868')
            GROUP BY adr_umls_cui) as adr_umls_cui_unique on adr_llt.adr_umls_cui = adr_umls_cui_unique.adr_umls_cui
            """
        return self._query_all(sql)

    def create(self, obj: AdrLlt) -> AdrLlt:
        pass

    def delete(self, external_id: str) -> None:
        pass