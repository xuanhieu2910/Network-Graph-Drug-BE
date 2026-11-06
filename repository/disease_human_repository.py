from repository.base_repository import BaseRepository
from model.disease_human import DiseaseHuman

class DiseaseHumanRepository(BaseRepository[DiseaseHuman]):

    def __init__(self, connection):
        super().__init__(connection, DiseaseHuman)

    def get_by_id(self, mondo_id: str) -> DiseaseHuman:
        sql = "SELECT * FROM disease_human WHERE mondo_id = %(mondo_id)s"
        return self._query_one(
            sql,
            {'mondo_id': mondo_id}
        )

    def get_all(self) -> list[DiseaseHuman]:
        sql = """
            select disease_human.* from disease_human
    inner join (select human_gene_disease.mondo_id from human_gene_disease
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
    group by human_gene_disease.mondo_id )as human_gene_disease on disease_human.mondo_id = human_gene_disease.mondo_id
            """
        return self._query_all(sql)

    def create(self, obj: DiseaseHuman) -> DiseaseHuman:
        sql = """
            INSERT INTO disease_human (mondo_id,disease_name)
                VALUES (
                        %(mondo_id)s,
                        %(disease_name)s
                    )
            """
        return self._execute(
            sql,
            obj.model_dump()
        )

    def delete(self,mondo_id: str) -> None:
        sql = "DELETE FROM disease_human WHERE mondo_id = %(mondo_id)s "
        self._execute(
            sql,
            {"mondo_id":mondo_id}
        )