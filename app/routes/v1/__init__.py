from fastapi import APIRouter

from .products import router as product_router

router_v1 = APIRouter(prefix='/v1')

router_v1.include_router(product_router)

