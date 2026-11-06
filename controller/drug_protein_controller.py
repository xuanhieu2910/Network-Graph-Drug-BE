from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Depends
from databases import get_connection
from services.drug_protein_service import DrugProteinService



drug_protein_router = APIRouter(prefix="/drug_protein", tags=["Drug Protein"])

@drug_protein_router.get("/find_all")
def find_all_proteins(connection=Depends(get_connection)):
    drug_protein_service = DrugProteinService(connection)
    data_drug_protein = drug_protein_service.find_all()
    if data_drug_protein is None:
            raise HTTPException(
                status_code=404,
                detail="protein not found"
            )
    return data_drug_protein


@drug_protein_router.get("/details/")
def find_protein_by_code(drug_code: str, protein_code: str, connection=Depends(get_connection)):
    drug_protein_service = DrugProteinService(connection)
    drug_protein_detail = drug_protein_service.find_by_id_drug_and_protein(
                                                drug_code=drug_code,
                                                protein_code = protein_code)

    if drug_protein_detail is None:
        raise HTTPException(
            status_code=404,
            detail="Drug Protein not found"
        )

    return drug_protein_detail
