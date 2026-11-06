from pydantic import BaseModel, ConfigDict

class ItemResponse(BaseModel):
    
    model_config = ConfigDict(from_attributes=True)
    name: str
    description: str = None
    price: float
    tax: float = None

    # def create_item_response(self, item_request):
    #     item_response = ItemResponse()

    #     item_response.name=item_request.name
    #     item_response.description=item_request.description
    #     item_response.price=item_request.price
    #     item_response.tax=item_request.tax
        
    #     return item_response