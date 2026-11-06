from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Depends
from databases import get_connection
from services.drugs_smiles_service import DrugSmilesService
from model.drugs_smiles import DrugsSmiles



drug_smile_router = APIRouter(prefix="/drug_smiles", tags=["Drug Smiles"])

@drug_smile_router.get("/find_all")
def find_all_drug_smiles(connection=Depends(get_connection)):
    drug_smiles_service = DrugSmilesService(connection)
    find_all = drug_smiles_service.find_all()
    if find_all is None:
            raise HTTPException(
                status_code=404,
                detail="drug_smiles not found"
            )
    return find_all


@drug_smile_router.get("/details/{external_id}")
def get_drug_smiles_by_id(external_id: str, connection=Depends(get_connection)):
    drug_smiles_service = DrugSmilesService(connection)
    drug_smiles = drug_smiles_service.find_by_id(external_id=external_id)

    if drug_smiles is None:
        raise HTTPException(
            status_code=404,
            detail="drug_smiles not found"
        )

    return drug_smiles
