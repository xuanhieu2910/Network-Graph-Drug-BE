from repository.base_repository import BaseRepository
from model.drug_adr_llt import DrugAdrLlt

class DrugAdrRepository(BaseRepository[DrugAdrLlt]):

    def __init__(self, connection):
        super().__init__(connection, DrugAdrLlt)

    def get_by_id(self, mondo_id: str) -> DrugAdrLlt:
        pass


    def get_all(self) -> list[DrugAdrLlt]:
        sql = """
           SELECT *
            FROM drug_adr_llt
            WHERE drug_bank_id in ('DB01254','DB04868')
            """
        return self._query_all(sql)

    def create(self, obj: DrugAdrLlt) -> DrugAdrLlt:
        sql = """
            INSERT INTO drug_adr_llt (drug_id, adr_id)
            VALUES (
                    %(drug_id)s,
                    %(adr_id)s
                )
            """
        return self._execute(
            sql,
            obj.model_dump()
        )

    def delete(self,mondo_id: str) -> None:
        pass