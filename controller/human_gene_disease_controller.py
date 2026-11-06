from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Depends
from databases import get_connection
from services.human_gene_disease_service import HumanGeneDiseaseService


human_gene_disease_service_router = APIRouter(prefix = "/human_gene_disease", tags = ["Human Gene Disease"])

@human_gene_disease_service_router.get("/find_all")
def find_all_human_gene_disease(connection = Depends(get_connection)):
    human_gene_disease_service = HumanGeneDiseaseService(connection)
    data_find_all = human_gene_disease_service.find_all()
    if data_find_all is None:
        raise HTTPException(
            status_code = 404,
            detail = "Human Gene Disease Not Found"
        )

    return data_find_all

@human_gene_disease_service_router.get("/details")
def find_human_gene_disease_service_by_hsa_and_mondo(hsa_code: str, mondo_code: str, connection=Depends(get_connection)):
    human_gene_disease_service = HumanGeneDiseaseService(connection)
    data_human_gene_disease_detail = human_gene_disease_service.find_by_id_hsa_and_mondo_id(hsa_code, mondo_code)

    if data_human_gene_disease_detail is None:
        raise HTTPException(
            status_code = 404,
            detail = "Human Gene Disease Detail Not Found"
        )

    return data_human_gene_disease_detail