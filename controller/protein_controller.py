from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Depends
from databases import get_connection
from services.proteins_service import ProteinService
from model.proteins import Protein



protein_router = APIRouter(prefix="/proteins", tags=["Proteins"])

@protein_router.get("/find_all")
def find_all_proteins(connection=Depends(get_connection)):
    protein_service = ProteinService(connection)
    data_proteins = protein_service.find_all()
    if data_proteins is None:
            raise HTTPException(
                status_code=404,
                detail="protein not found"
            )
    return data_proteins


@protein_router.get("/details/{protein_code}")
def find_protein_by_code(protein_code: str, connection=Depends(get_connection)):
    protein_service = ProteinService(connection)
    protein_detail = protein_service.get_by_code(protein_code=protein_code)

    if protein_detail is None:
        raise HTTPException(
            status_code=404,
            detail="protein_detail not found"
        )

    return protein_detail
