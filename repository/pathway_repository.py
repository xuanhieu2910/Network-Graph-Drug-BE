from repository.base_repository import BaseRepository
from model.pathway import Pathway


class PathwayRepository(BaseRepository[Pathway]):

    def __init__(self, connection):
        super().__init__(connection, Pathway)

    def get_by_id(self, id: str):
        sql = "SELECT * FROM pathway WHERE pathway_id = %(pathway_id)s"
        return self._query_one(
            sql,
            {
                'pathway_id': id
            }
        )

    def get_all(self) -> list[Pathway]:
        sql = """
            select * from pathway
            inner join
        (select kegg_pathway.pathway_id from kegg_pathway
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
        group by kegg_pathway.pathway_id) kegg_pathway on pathway.pathway_id = kegg_pathway.pathway_id
        """
        return self._query_all(sql)

    def create(self, obj: Pathway) -> Pathway:
        sql = """
            INSERT
            INTO pathway (pathway_id, pathway_name)
            VALUES (%(pathway_id)s,
                    %(pathway_name)s)
                )
            """ 
        return self._execute(sql, obj.model_dump())

    def delete(self, id: str):
        pass
    