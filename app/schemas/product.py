from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: int
    name: str
    image_url: str
    description: str
    price: int
