from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Depends
from databases import get_connection
from services.kegg_pathway_service import KeggPathwayService


kegg_pathway_router = APIRouter(prefix="/kegg_gene_pathway", tags=["Kegg Gene Pathway"])


@kegg_pathway_router.get("/find_all")
def find_all_kegg_pathway(connection=Depends(get_connection)):
    kegg_pathway_service = KeggPathwayService(connection)
    data_pathway_element = kegg_pathway_service.find_all()
    if data_pathway_element is None:
            raise HTTPException(
                status_code=404,
                detail="Kegg pathway not found"
            )
    return data_pathway_element

@kegg_pathway_router.get("/details/")
def find_kegg_pathway_by_hsa_code_and_pathway_id(hsa_code: str, pathway_id: str,
                               connection=Depends(get_connection)):
    kegg_pathway_service = KeggPathwayService(connection)
    data_pathway_element_detail = kegg_pathway_service.find_by_hsa_code_and_pathway_id(hsa_code, pathway_id)

    if data_pathway_element_detail is None:
        raise HTTPException(
            status_code=404,
            detail="Kegg pathway not found"
        )

    return data_pathway_element_detail
