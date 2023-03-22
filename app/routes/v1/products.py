from fastapi import APIRouter
from typing import List

from ...services import product_service
from ...schemas.product import ProductResponse

router = APIRouter(prefix='/products')

@router.get('/')
async def get_products() -> List[ProductResponse]:
    response = product_service.get_all_products()
    return response