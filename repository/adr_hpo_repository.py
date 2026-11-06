from repository.base_repository import BaseRepository
from model.adr_hpo import AdrHpo

class AdrHpoRepository(BaseRepository[AdrHpo]):

    def __init__(self, connection):
        super().__init__(connection, AdrHpo)

    def get_by_id(self, mondo_id: str) -> AdrHpo:
        pass


    def get_all(self) -> list[AdrHpo]:
        sql = """
           SELECT adr_hpo.*
            FROM adr_hpo
                inner join (SELECT adr_umls_cui
                            FROM drug_adr_llt
                            WHERE drug_bank_id in ('DB01254','DB04868')
                            GROUP BY adr_umls_cui) as adr_umls_cui_unique on adr_hpo.adr_umls_cui = adr_umls_cui_unique.adr_umls_cui
            """
        return self._query_all(sql)

    def create(self, obj: AdrHpo) -> AdrHpo:
        sql = """
            INSERT INTO adr_hpo (adr_umls_cui, hpo_id)
            VALUES (
                    %(adr_umls_cui)s,
                    %(hpo_id)s
                )
            """
        return self._execute(
            sql,
            obj.model_dump()
        )

    def delete(self,mondo_id: str) -> None:
        pass