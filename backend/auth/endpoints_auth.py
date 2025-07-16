from fastapi import APIRouter
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from starlette.requests import Request

from auth.models import User
from auth.schemas import RegisterUserRequestSchema
from auth.security import manager, pwd_context, limiter
from core.database import create_session

router = APIRouter()


@manager.user_loader()
def query_user(email: str):
    return create_session().query(User).filter(User.email == email).first()


@router.post("/register")
@limiter.limit("50/minute")
async def register(request: Request, user: RegisterUserRequestSchema):
    db = create_session()
    existing_user = db.query(User).filter_by(email=user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User is already registered.")
    user.password = pwd_context.hash(user.password)
    user_data = user.model_dump()
    user_data['role'] = 'user'
    new_user = User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user.id


@router.post("/login")
@limiter.limit("50/minute")
def login(request: Request, data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password

    user = query_user(username)
    if not user:
        raise InvalidCredentialsException
    elif not pwd_context.verify(password, user.password):
        raise InvalidCredentialsException

    access_token = manager.create_access_token(data={"sub": username})
    return {"access_token": access_token}