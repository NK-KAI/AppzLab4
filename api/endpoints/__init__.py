from .user import router as user_router
from .announcement import router as announcement_router
from .category import router as category_router
from .subcategory import router as subcategory_router
from .tag import router as tag_router

__routers__ = [
    user_router,
    announcement_router,
    category_router,
    subcategory_router,
    tag_router,
]
