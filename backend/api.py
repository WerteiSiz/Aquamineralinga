from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from auth.security import limiter
from auth.endpoints_user import router as user_router
from auth.endpoints_auth import router as auth_router
from terrain.endpoints import router as terrain_router

app = FastAPI(title='Aquamaringa')

app.include_router(auth_router, prefix="/auth", tags=("Auth",))
app.include_router(user_router, prefix="/user", tags=("User",))
app.include_router(terrain_router, prefix="/terrain", tags=("Terrain",))

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
