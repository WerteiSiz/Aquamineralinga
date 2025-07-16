from pydantic import BaseModel


class RegisterUserRequestSchema(BaseModel):
    username: str | None = None
    email: str
    password: str


class SettingUserRequestSchema(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None


class SettingUserResponseSchema(BaseModel):
    username: str
    email: str
    password: str


class DeleteUserRequestSchema(BaseModel):
    password: str


class DeleteUserResponseSchema(BaseModel):
    detail: str