from repository.base_repository import BaseRepository
from model.unit_protein_kegg_gene import UnitProteinKeggGene

class UnitProteinKeggGeneRepository(BaseRepository[UnitProteinKeggGene]):

    def __init__(self, connection):
        super().__init__(connection, UnitProteinKeggGene)

    def get_by_id(self, protein_code: str) -> UnitProteinKeggGene:
        sql = "SELECT * FROM unit_protein_kegg_gene WHERE code = %(protein_code)s"
        return self._query_one(
            sql,
            {
                "protein_code": protein_code
            }
        )

    def get_all(self) -> list[UnitProteinKeggGene]:
        sql = """
        select unit_protein_kegg_gene.*
        from unit_protein_kegg_gene
                inner join (SELECT proteins.unit_protein_id
                            FROM proteins
                                    inner join (SELECT unit_protein_id, drug_bank_id
                                                FROM drug_protein
                                                where drug_bank_id in (
                                                                        'DB01254',
                                                                        'DB04868')) protein_new
                                                on proteins.unit_protein_id = protein_new.unit_protein_id) protein
                            on unit_protein_kegg_gene.uniprot_id = protein.unit_protein_id
                    """
        return self._query_all(sql)

    def create(self, obj: UnitProteinKeggGene) -> UnitProteinKeggGene:
        sql = """
            INSERT INTO unit_protein_kegg_gene (code, uniprot_id, kegg_gene)
            VALUES ( %(code)s, 
                    %(uniprot_id)s, 
                    %(kegg_gene)s) 
            """
        return self._execute(
            sql,
            obj.model_dump()
        )

    def delete(self,mondo_id: str) -> None:
        pass