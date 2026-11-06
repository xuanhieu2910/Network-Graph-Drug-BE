from repository.base_repository import BaseRepository
from model.adr_llt import AdrLlt

class AdrLltRepository(BaseRepository[AdrLlt]):
    
    def __init__(self, connection):
        super().__init__(connection, AdrLlt)

    def get_by_id(self, external_id: str) -> AdrLlt:
        pass


    def get_all(self) -> list[AdrLlt]:
        sql = """
            select adr_llt.*
            from drugs_smiles
                inner join drug_adr_llt on drugs_smiles.external_id = drug_adr_llt.drug_bank_id
                inner join adr_llt on drug_adr_llt.adr_umls_cui = adr_llt.adr_umls_cui
            where external_id in ('DB01254', 'DB04868')
            """
        return self._query_all(sql)

    def create(self, obj: AdrLlt) -> AdrLlt:
        pass

    def delete(self, external_id: str) -> None:
        pass