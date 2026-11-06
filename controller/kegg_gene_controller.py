from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Depends
from databases import get_connection
from services.kegg_gene_service import KeggGeneService


kegg_gene_router = APIRouter(prefix="/kegg_gene", tags=["Kegg Gene"])


@kegg_gene_router.get("/find_all")
def find_all_kegg_gene(connection=Depends(get_connection)):
    kegg_gene_service = KeggGeneService(connection)
    data_gene_element = kegg_gene_service.find_all()
    if data_gene_element is None:
            raise HTTPException(
                status_code=404,
                detail="Kegg gene not found"
            )
    return data_gene_element

@kegg_gene_router.get("/details/")
def find_kegg_gene_by_hsa_code(hsa_code: str,
                               connection=Depends(get_connection)):
    kegg_gene_service = KeggGeneService(connection)
    kegg_gene_detail = kegg_gene_service.find_by_hsa_code(hsa_code)

    if kegg_gene_detail is None:
        raise HTTPException(
            status_code=404,
            detail="Kegg Kegg gene not found"
        )

    return kegg_gene_detail
