from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Depends
from databases import get_connection
from services.kegg_disease_service import KeggDiseaseService
from model.kegg_disease import KeggDisease

kegg_disease_router = APIRouter(prefix="/kegg_disease_router", tags=["Kegg Disease Router"])


@kegg_disease_router.get("/find_all")
def find_all_kegg_diease(connection=Depends(get_connection)):
    kegg_diease_service = KeggDiseaseService(connection)
    data_kegg_diease = kegg_diease_service.find_all()
    if data_kegg_diease is None:
            raise HTTPException(
                status_code=404,
                detail="protein not found"
            )
    return data_kegg_diease


@kegg_disease_router.get("/details")
def find_kegg_diease_router(hsa_code: str, diease_id: str, connection=Depends(get_connection)):
    kegg_diease_service = KeggDiseaseService(connection)
    data_kegg_diease_detail = kegg_diease_service.find_by_hsa_code_and_diease_id(hsa_code, diease_id)

    if data_kegg_diease_detail is None:
        raise HTTPException(
            status_code = 404,
            detail = "Kegg Diease Detail Not Found"
        )

    return data_kegg_diease_detail