from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Depends
from databases import get_connection
from services.pathway_service import PathwayService


pathway_router = APIRouter(prefix="/pathway", tags=["Pathway"])


@pathway_router.get("/find_all")
def find_all_pathway(connection=Depends(get_connection)):
    pathway_service = PathwayService(connection)
    data_pathway = pathway_service.find_all()
    if data_pathway is None:
            raise HTTPException(
                status_code=404,
                detail="Pathway not found"
            )
    return data_pathway

@pathway_router.get("/details/")
def find_pathway_by_pathway_id( pathway_id: str,
                               connection=Depends(get_connection)):
    pathway_service = PathwayService(connection)
    data_pathway_element_detail = pathway_service.find_by_pathway_id(pathway_id)

    if data_pathway_element_detail is None:
        raise HTTPException(
            status_code=404,
            detail="Pathway not found"
        )

    return data_pathway_element_detail
