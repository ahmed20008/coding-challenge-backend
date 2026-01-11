from api.applications import create, detail
from fastapi import APIRouter
from api.applications import list, pdf

router = APIRouter(prefix="/applications", tags=["applications"])

router.include_router(create.router)
router.include_router(list.router)
router.include_router(detail.router)
router.include_router(pdf.router)
