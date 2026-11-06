from fastapi import FastAPI
from responsive.item_response import ItemResponse
from fastapi.middleware.cors import CORSMiddleware
from controller.drug_smiles_controller import drug_smile_router
from controller.protein_controller import protein_router
from controller.drug_protein_controller import drug_protein_router
from controller.disease_human_controller import disease_human_router
from controller.human_gene_disease_controller import human_gene_disease_service_router
from controller.human_phenotype_ontology_controller import human_phenotype_ontology_router
from controller.kegg_diease_controller import kegg_disease_router
from controller.kegg_element_controller import kegg_element_router
from controller.kegg_gene_controller import kegg_gene_router
from controller.kegg_pathway_controller import kegg_pathway_router
from controller.pathway_controller import pathway_router
from controller.unit_protein_kegg_gene_controller import unit_protein_kegg_gene_router
from controller.adr_hpo_controller import adr_hpo_router
from controller.adr_llt_controller import adr_llt_router
from controller.drug_adr_controller import drug_adr_router
from controller.mondo_human_phenotype_controller import mondo_human_phenotype_router



app = FastAPI()

app.include_router(drug_smile_router)
app.include_router(protein_router)
app.include_router(drug_protein_router)
app.include_router(disease_human_router)
app.include_router(human_gene_disease_service_router)
app.include_router(human_phenotype_ontology_router)
app.include_router(kegg_disease_router)
app.include_router(kegg_element_router)
app.include_router(kegg_gene_router)
app.include_router(kegg_pathway_router)
app.include_router(pathway_router)
app.include_router(unit_protein_kegg_gene_router)
app.include_router(adr_hpo_router)
app.include_router(adr_llt_router)
app.include_router(drug_adr_router)
app.include_router(mondo_human_phenotype_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"]
)