from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Depends
from databases import get_connection
from services.mondo_human_phenotype_service import MondoHumanPhenotypeService


mondo_human_phenotype_router = APIRouter(prefix = "/mondo_human_phenotype", tags = ["Mondo Human Phenotype"])

@mondo_human_phenotype_router.get("/find_all")
def find_all_mondo_human_phenotype(connection = Depends(get_connection)):
    mondo_human_phenotype_service = MondoHumanPhenotypeService(connection)
    data_find_all = mondo_human_phenotype_service.find_all()
    if data_find_all is None:
        raise HTTPException(
            status_code = 404,
            detail = "Mondo Human Phenotype Not Found"
        )

    return data_find_all

@mondo_human_phenotype_router.get("/details")
def find_mondo_human_phenotype_by_id(id: str, connection=Depends(get_connection)):
    mondo_human_phenotype_service = MondoHumanPhenotypeService(connection)
    data_mondo_human_phenotype_detail = mondo_human_phenotype_service.find_by_id(id)

    if data_mondo_human_phenotype_detail is None:
        raise HTTPException(
            status_code = 404,
            detail = "Mondo Human Phenotype Detail Not Found"
        )

    return data_mondo_human_phenotype_detail