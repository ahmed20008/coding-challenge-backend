from fastapi import APIRouter
from api import create, list, detail

# Create main router
router = APIRouter(prefix="/applications", tags=["applications"])

# Include all sub-routers
router.include_router(create.router)
router.include_router(list.router)
router.include_router(detail.router)
