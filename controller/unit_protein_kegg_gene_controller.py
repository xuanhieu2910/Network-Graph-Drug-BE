from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Depends
from databases import get_connection
from services.unit_protein_kegg_gene_service import UnitProteinKeggGeneService


unit_protein_kegg_gene_router = APIRouter(prefix="/unit_protein_kegg_gene", tags=["Unit Protein Kegg Gene"])


@unit_protein_kegg_gene_router.get("/find_all")
def find_all_unit_protein_kegg_gene(connection=Depends(get_connection)):
    unit_protein_kegg_gene_service = UnitProteinKeggGeneService(connection)
    data_unit_protein_kegg_gene = unit_protein_kegg_gene_service.find_all()
    if data_unit_protein_kegg_gene is None:
            raise HTTPException(
                status_code=404,
                detail="Unit protein kegg not found"
            )
    return data_unit_protein_kegg_gene

@unit_protein_kegg_gene_router.get("/details/")
def find_unit_protein_kegg_gene_by_code_protein(protein_code: str,
                               connection=Depends(get_connection)):
    unit_protein_kegg_gene_service = UnitProteinKeggGeneService(connection)
    data_unit_protein_kegg_gene_detail = unit_protein_kegg_gene_service.get_by_code(protein_code)

    if data_unit_protein_kegg_gene_detail is None:
        raise HTTPException(
            status_code=404,
            detail="Unit protein kegg not found"
        )

    return data_unit_protein_kegg_gene_detail
