from repository.base_repository import BaseRepository
from model.drugs_smiles import DrugsSmiles

class DrugSmilesRepository(BaseRepository[DrugsSmiles]):
    
    def __init__(self, connection):
        super().__init__(connection, DrugsSmiles)

    def get_by_id(self, external_id: str) -> DrugsSmiles:
        sql = "SELECT * FROM drugs_smiles WHERE external_id = %(external_id)s"
        return self._query_one(sql,  {
        "external_id": external_id
    })


    def get_all(self) -> list[DrugsSmiles]:
        sql = """
            select * from drugs_smiles
            where external_id in (
            'DB01254',
            'DB04868')
            """
        return self._query_all(sql)

    def create(self, obj: DrugsSmiles) -> DrugsSmiles:
        sql = """
            INSERT INTO drugs_smiles (sid, 
                                    data_source,
                                    external_id,
                                    synonyms,
                                    data_source_category,
                                    compound_cid,
                                    name,
                                    smiles)
            VALUES (%(sid)s, 
            %(data_source)s, 
            %(external_id)s, 
            %(synonyms)s, 
            %(data_source_category)s, 
            %(compound_cid)s,
            %(name)s, 
            %(smiles)s
            )
        """
        return self._execute(sql, obj.model_dump())

    def delete(self, external_id: str) -> None:
        sql = "DELETE FROM drugs_smiles WHERE external_id = %(external_id)s"
        self._execute(sql, {"external_id": external_id})