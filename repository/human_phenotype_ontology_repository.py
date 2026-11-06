from repository.base_repository import BaseRepository
from model.human_phenotype_ontology import HumanPhenotypeOntology

class HumanPhenotypeOntologyRepository(BaseRepository[HumanPhenotypeOntology]):
    
    def __init__(self, connection):
        super().__init__(connection, HumanPhenotypeOntology)

    def get_by_id(self, id: str) -> HumanPhenotypeOntology:
        sql = """
            select *
            from human_phenotype_ontology
            where hpo_id = % (hpo_id)s 
            """        
        return self._query_one(
            sql,
            {
             'hpo_id' : id   
            }
        )

    def get_all(self) -> list[HumanPhenotypeOntology]:
        sql =  """
            select human_phenotype_ontology.* from human_phenotype_ontology
            inner join
            (select disease_to_human_phenotype_ontology.database_id
            from disease_to_human_phenotype_ontology
                    inner join (select disease_human.*
                                from disease_human
                                        inner join (select human_gene_disease.mondo_id
                                                    from human_gene_disease
                                                            inner join (select unit_protein_kegg_gene.kegg_gene
                                                                        from unit_protein_kegg_gene
                                                                                    inner join (SELECT proteins.unit_protein_id
                                                                                                FROM proteins
                                                                                                        inner join (SELECT unit_protein_id, drug_bank_id
                                                                                                                    FROM drug_protein
                                                                                                                    where
                                                                                                                        drug_bank_id in
                                                                                                                        (
                                                                                                                        'DB01254',
                                                                                                                        'DB04868')) protein_new
                                                                                                                    on proteins.unit_protein_id = protein_new.unit_protein_id) protein
                                                                                            on unit_protein_kegg_gene.uniprot_id = protein.unit_protein_id
                                                                        group by unit_protein_kegg_gene.kegg_gene) as kegg_finding
                                                                        on human_gene_disease.hsa = kegg_finding.kegg_gene
                                                    group by human_gene_disease.mondo_id) as human_gene_disease
                                                    on disease_human.mondo_id = human_gene_disease.mondo_id) as disease_human on disease_to_human_phenotype_ontology.mondo_id = disease_human.mondo_id
            group by database_id) as hpo on human_phenotype_ontology.hpo_id = hpo.database_id
            """
        return self._query_all(
            sql
        )

    def create(self, obj: HumanPhenotypeOntology) -> HumanPhenotypeOntology:
        sql = """           
            INSERT
            INTO human_phenotype_ontology (hpo_id, hpo_name)
            VALUES (%(hpo_id)s,
                    %(hpo_name)s)
            """
        return self._execute(sql, obj.model_dump())

    def delete(self, id: str) -> None:
        sql = "DELETE  FROM human_phenotype_ontology WHERE hpo_id = %(hpo_id)s "
        self._execute(
            sql,
            {
                'hpo_id': id
            }
        )


