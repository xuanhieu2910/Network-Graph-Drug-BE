from repository.base_repository import BaseRepository
from model.proteins import Protein

class ProteinRepository(BaseRepository[Protein]):

    def __init__(self, connection):
        super().__init__(connection, Protein)

    def get_by_id(self, protein_code: str) -> Protein:
        sql = "SELECT * FROM proteins WHERE unit_protein_id = %(code)s"
        return self._query_one(
            sql, 
            {'code':protein_code}
        )

    def get_all(self) -> list[Protein]:
        sql = """
            SELECT proteins.* FROM proteins
            inner join (
            SELECT unit_protein_id, drug_bank_id
            FROM drug_protein
            where drug_bank_id in (
                                'DB04868',
                                'DB01254')) protein_new
            on proteins.unit_protein_id = protein_new.unit_protein_id
            """
        return self._query_all(sql)

    def create(self, obj: Protein) -> Protein:
        sql = """
            INSERT INTO proteins (name,
                      unit_protein_id)
            VALUES (%(name)s,
                    %(unit_protein_id)s
                    )
            """
        return self._execute(
            sql,
            obj.model_dump()
        )

    def delete(self, protein_code: str) -> None:
        sql = "DELETE FROM proteins WHERE unit_protein_id = %(unit_protein_id)s"
        self._execute(
            sql,
            {"unit_protein_id":protein_code}
        )