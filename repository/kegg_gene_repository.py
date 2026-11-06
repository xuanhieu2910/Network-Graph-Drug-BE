from repository.base_repository import BaseRepository
from model.kegg_gene import KeggGene

class KeggGeneRepository(BaseRepository[KeggGene]):
    def __init__(self, connection):
        super().__init__(connection, KeggGene)

    def get_by_id(self, id: str) -> KeggGene:
        sql = "SELECT * FROM kegg_gene WHERE kegg_hsa = %(hsa_code)s "
        return self._query_one(
            sql,
            {
                "hsa_code": id
            }
        )

    def get_all(self) -> list[KeggGene]:
        sql = """
                select * from kegg_gene
    inner join (select unit_protein_kegg_gene.kegg_gene
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
         group by unit_protein_kegg_gene.kegg_gene) as kegg_finding on kegg_gene.kegg_hsa = kegg_finding.kegg_gene
        """
        return self._query_all(sql)


    def create(self, obj: KeggGene) -> KeggGene:
        sql = """
            INSERT 
            INTO kegg_gene (kegg_hsa, kegg_entry, 
                            kegg_symbol, kegg_name, 
                            kegg_orthology, kegg_organism)
            VALUES ( %(kegg_hsa)s, 
                    %(kegg_entry)s, 
                    %(kegg_symbol)s, 
                    %(kegg_name)s, 
                    %(kegg_orthology)s, 
                    %(kegg_organism)s)
            """
        return self._execute(sql, obj.model_dump())

    def delete(self, id: str):
        pass