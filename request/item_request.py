from pydantic import BaseModel, ConfigDict

class ItemRequest(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
