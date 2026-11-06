from repository.base_repository import BaseRepository
from model.kegg_pathway import KeggPathway


class KeggPathwayRepository(BaseRepository[KeggPathway]):

    def __init__(self, connection):
        super().__init__(connection, KeggPathway)

    def get_by_id(self, id: str):
        pass

    def get_by_hsa_code_and_pathway_id(self, hsa_code: str, pathway_id: str) -> KeggPathway:
        sql = """
            SELECT * FROM kegg_pathway WHERE kegg_hsa = %(hsa_code)s and pathway_id = %(pathway_id)s
            """
        return self._query_one(
            sql,
            {
                "hsa_code": hsa_code,
                "pathway_id": pathway_id
            }
        )

    def get_all(self) -> list[KeggPathway]:
        sql = """
                select * from kegg_pathway
                inner join (select kegg_gene.kegg_hsa from kegg_gene
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
                    group by unit_protein_kegg_gene.kegg_gene) as kegg_finding on kegg_gene.kegg_hsa = kegg_finding.kegg_gene) kegg_gene
                    on kegg_pathway.kegg_hsa = kegg_gene.kegg_hsa

        """
        return self._query_all(sql)

    def create(self, obj: KeggPathway) -> KeggPathway:
        sql = """
            INSERT
            INTO kegg_pathway (kegg_hsa, pathway_id, pathway_name)
            VALUES ( %(kegg_hsa)s, 
                    %(pathway_id)s, 
                    %(pathway_name)s)
                )
            """ 
        return self._execute(sql, obj.model_dump())

    def delete(self, id: str):
        pass
    