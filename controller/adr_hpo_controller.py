from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Depends
from databases import get_connection
from services.adr_hpo_service import AdrHpoService


adr_hpo_router = APIRouter(prefix="/adr_hpo", tags=["ADR HPO"])


@adr_hpo_router.get("/find_all")
def find_all_adr_hpo(connection = Depends(get_connection)):
    adr_hpo_service = AdrHpoService(connection)
    data_adr_hpo_service = adr_hpo_service.find_all()
    if data_adr_hpo_service is None:
        raise HTTPException(
            status_code = 404,
            detail = "ADR HPO Not Found"
        )

    return data_adr_hpo_service


@adr_hpo_router.get("/details/")
def find_adr_hpo_by_id(adr_umls_cui: str, connection=Depends(get_connection)):
    adr_hpo_service = AdrHpoService(connection)
    data_adr_hpo_detail = adr_hpo_service.find_by_adr_umls_cui(adr_umls_cui)

    if data_adr_hpo_detail is None:
        raise HTTPException(
            status_code = 404,
            detail = "ADR HPO Detail Not Found"
        )

    return data_adr_hpo_detail