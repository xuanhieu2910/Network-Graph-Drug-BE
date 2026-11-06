from repository.base_repository import BaseRepository
from model.drug_protein import DrugProtein

class DrugProteinRepository(BaseRepository[DrugProtein]):

    def __init__(self, connection):
        super().__init__(connection, DrugProtein)

    def get_by_id():
        pass

    def get_all(self) -> list[DrugProtein]:
        sql = """
        SELECT unit_protein_id, drug_bank_id
        FROM drug_protein
        where drug_bank_id in (
                            'DB01254',
                            'DB04868')
            """
        return self._query_all(sql)

    def create(self, obj: DrugProtein) -> DrugProtein:
        sql = """
             INSERT INTO drug_protein(unit_protein_id, drug_bank_id)
            VALUES ( %(unit_protein_id)s,
                    %(drug_bank_id)s
                )
            """
        return self._execute(sql, obj.model_dump())
    

    def delete():
        pass

    def get_by_id_drug_and_protein(self, drug_id: str, protein_id: str) -> DrugProtein:
        sql = """
            SELECT unit_protein_id, drug_bank_id
            FROM drug_protein
            WHERE drugbank_id = %(drugbank_id)s
                        AND unit_protein_id = %(protein_code)s      
        """
        return self._query_one(
            sql,
            {
                'drugbank_id': drug_id,
                'protein_code': protein_id
            }
        )

    def delete_by_id_drug_or_protein(self, drug_id: str, protein_id: str):
        sql = "DELETE FROM drug_protein WHERE drugbank_id = %(drugbank_id)s or unit_protein_id = %(unit_protein_id)s"
        self._execute(
                    sql,
                    {
                        'drugbank_id': drug_id,
                        'unit_protein_id': protein_id
                    }
                )
