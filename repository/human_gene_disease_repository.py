from repository.base_repository import BaseRepository
from model.human_gene_disease import HumanGenDisease


class HumanGeneDiseaseRepository(BaseRepository[HumanGenDisease]):

    def __init__(self, connection):
        super().__init__(connection, HumanGenDisease)

    def get_by_id(self, id: str):
        pass

    def get_by_id_hsa_and_mondo(self, hsa_code: str, mond_code: str) -> HumanGenDisease:
        sql = """
            SELECT *
            FROM human_gene_disease
            WHERE hsa = %(hsa)s 
            and mondo_id = %(mondo_id)s
            """
        return self._query_one(
            sql,
            {
                "hsa": hsa_code,
                "mondo_id": mond_code
            }
        )

    def get_all(self) -> list[HumanGenDisease]:
        sql = """
        select human_gene_disease.* from human_gene_disease
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
                                group by unit_protein_kegg_gene.kegg_gene) as kegg_finding on human_gene_disease.hsa = kegg_finding.kegg_gene
            """
        return self._query_all(sql)

    def create(self, obj: HumanGenDisease) -> HumanGenDisease:
        sql = """
            INSERT
            INTO human_gene_disease (hsa, association_type, mondo_id)
            VALUES (
                    %(hsa)s,
                    %(association_type)s,
                    %(mondo_id)s
                )
            """ 
        return self._execute(sql, obj.model_dump())

    def delete(self, id: str):
        pass

    def delete_by_hsa_and_mondo(self, hsa: str, mondo_id: str) -> None:
        sql = "DELETE FROM human_gene_disease WHERE hsa = %(hsa)s and mondo_id = %(mondo_id)s"
        self._execute(
            sql,
            {
                'hsa': hsa,
                'mondo_id': mondo_id
            }
        )

    