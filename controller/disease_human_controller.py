from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Depends
from databases import get_connection
from services.disease_human_service import DiseaseHumanService


disease_human_router = APIRouter(prefix="/disease_human", tags=["Disease Human"])


@disease_human_router.get("/find_all")
def find_all_disease_human(connection = Depends(get_connection)):
    disease_human_service = DiseaseHumanService(connection)
    data_disease_human_service = disease_human_service.find_all()
    if data_disease_human_service is None:
        raise HTTPException(
            status_code = 404,
            detail = "Disease Human Not Found"
        )

    return data_disease_human_service


@disease_human_router.get("/details/")
def find_disease_human_by_id(mondo_code: str, connection=Depends(get_connection)):
    disease_human_service = DiseaseHumanService(connection)
    data_disease_human_detail = disease_human_service.find_by_mondo_id(mondo_code)

    if data_disease_human_detail is None:
        raise HTTPException(
            status_code = 404,
            detail = "Disease Human Detail Not Found"
        )

    return data_disease_human_detail