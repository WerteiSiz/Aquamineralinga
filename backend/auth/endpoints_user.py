from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import scoped_session
from starlette import status
from starlette.requests import Request

from auth.models import User
from auth.schemas import DeleteUserRequestSchema, DeleteUserResponseSchema, SettingUserResponseSchema, \
    SettingUserRequestSchema
from auth.security import manager, limiter
from auth.security import pwd_context
from core.database import get_session

router = APIRouter()


@router.patch("/settings", response_model=SettingUserResponseSchema)
async def update_settings(
        request: Request,
        data: SettingUserRequestSchema,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    us = db.query(User).get(user.id)
    obj_data = jsonable_encoder(us)
    update_data = data.model_dump(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(us, field, update_data[field])
    us.password = pwd_context.hash(us.password)
    db.add(us)
    db.commit()
    db.refresh(us)
    return us


def admin_only(user=Depends(manager)):
    if user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )
    return user


@router.post("/users/{user_id}/make-admin")
async def make_admin(
        user_id: UUID,
        db: scoped_session = Depends(get_session),
        current_user=Depends(admin_only)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.role = "admin"
    db.commit()
    return {"detail": f"User {user.email} is now an admin"}


@router.delete("/settings", response_model=DeleteUserResponseSchema)
async def delete_account(
        request: Request,
        data: DeleteUserRequestSchema,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    us = db.query(User).get(user.id)
    if not us:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    if not pwd_context.verify(data.password, us.password):
        raise HTTPException(status_code=400, detail="Неверный пароль")

    db.delete(us)
    db.commit()
    return {"detail": "Аккаунт успешно удален"}
