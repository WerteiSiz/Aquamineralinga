import os

from fastapi_login import LoginManager

from passlib.context import CryptContext
from slowapi import Limiter
from slowapi.util import get_remote_address

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET = "wN2Zxb7HtrD5BaYoy5IhNEioME15HafrHpGdEAELs1Hx99yo4lP/aGwF"
manager = LoginManager(SECRET, "/login")

limiter = Limiter(key_func=get_remote_address)
