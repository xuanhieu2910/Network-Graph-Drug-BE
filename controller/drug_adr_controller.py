from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Depends
from databases import get_connection
from model import adr_llt
from services.adr_llt_service import AdrLltService
from model.drug_adr_llt import DrugAdrLlt
from services.drug_adr_service import DrugAdrService
from services.drugs_smiles_service import DrugSmilesService



drug_adr_router = APIRouter(prefix="/drug_adr", tags=["Drug ADR"])

@drug_adr_router.get("/find_all")
def find_all_drug_adr(connection=Depends(get_connection)):
    drug_adr_service = DrugAdrService(connection)
    find_all = drug_adr_service.find_all()
    if find_all is None:
            raise HTTPException(
                status_code=404,
                detail="drug_adr not found"
            )
    return find_all


@drug_adr_router.get("/details/{external_id}")
def get_drug_adr_by_id(external_id: str, connection=Depends(get_connection)):
    drug_adr_service = DrugAdrService(connection)
    drug_adr = drug_adr_service.find_by_id(external_id=external_id)

    if drug_adr is None:
        raise HTTPException(
            status_code=404,
            detail="drug_adr not found"
        )

    return drug_adr
