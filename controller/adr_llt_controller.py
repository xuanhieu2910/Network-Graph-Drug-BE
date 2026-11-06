from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Depends
from databases import get_connection
from services.adr_llt_service import AdrLltService
from model.adr_llt import AdrLlt
from services.drugs_smiles_service import DrugSmilesService



adr_llt_router = APIRouter(prefix="/adr_llt", tags=["ADR LLT"])

@adr_llt_router.get("/find_all")
def find_all_adr_llt(connection=Depends(get_connection)):
    adr_llt_service = AdrLltService(connection)
    find_all = adr_llt_service.find_all()
    if find_all is None:
            raise HTTPException(
                status_code=404,
                detail="adr_llt not found"
            )
    return find_all


@adr_llt_router.get("/details/{external_id}")
def get_adr_llt_by_id(external_id: str, connection=Depends(get_connection)):
    adr_llt_service = AdrLltService(connection)
    adr_llt = adr_llt_service.find_by_id(external_id=external_id)

    if adr_llt is None:
        raise HTTPException(
            status_code=404,
            detail="adr_llt not found"
        )

    return adr_llt
