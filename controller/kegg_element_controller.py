from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Depends
from databases import get_connection
from services.kegg_element_service import KeggElementService


kegg_element_router = APIRouter(prefix="/kegg_element", tags=["Kegg Element"])


@kegg_element_router.get("/find_all")
def find_all_kegg_element(connection=Depends(get_connection)):
    kegg_element_service = KeggElementService(connection)
    data_kegg_element = kegg_element_service.find_all()
    if data_kegg_element is None:
            raise HTTPException(
                status_code=404,
                detail="Kegg element not found"
            )
    return data_kegg_element

@kegg_element_router.get("/details/")
def find_kegg_element_by_hsa_code_and_element_id(hsa_code: str, 
                                                 element_id: str,
                                                   connection=Depends(get_connection)):
    kegg_element_service = KeggElementService(connection)
    kegg_element_detail = kegg_element_service.find_by_hsa_code_and_element_id(
                                                hsa_code=hsa_code,
                                                element_id=element_id)

    if kegg_element_detail is None:
        raise HTTPException(
            status_code=404,
            detail="Kegg element not found"
        )

    return kegg_element_detail
