from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Depends
from databases import get_connection
from services.human_phenotype_ontology_service import HumanPhenotypeOntologyService

human_phenotype_ontology_router =  APIRouter(prefix = "/human_phenotype_ontology", tags = ["Human Phenotype Ontology"])

@human_phenotype_ontology_router.get("/find_all")
def find_all_human_phenotype_ontology_router(connection = Depends(get_connection)):
    human_phenotype_ontology_service = HumanPhenotypeOntologyService(connection)
    data_find_all = human_phenotype_ontology_service.find_all()
    if data_find_all is None:
        raise HTTPException(
            status_code = 404,
            detail = "Human Phenotype Ontology Not Found"
        )

    return data_find_all

@human_phenotype_ontology_router.get("/details")
def find_human_phenotype_ontology_router_by_id(id_human_phenotype: str, 
                                               connection=Depends(get_connection)):
    human_phenotype_ontology_service = HumanPhenotypeOntologyService(connection)
    data_detail = human_phenotype_ontology_service.find_by_id_human_phenotype_ontology(id_human_phenotype)
    if data_detail is None:
        raise HTTPException(
            status_code = 404,
            detail = "Human Phenotype Ontology Detail Not Found"
        )

    return data_detail