from typing import Annotated

from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.auth import Token, authRegister, authBaseRegister
from app.clients import auth_service
from fastapi import APIRouter, Depends

router = APIRouter()

@router.post("/post", response_model=authBaseRegister)
def register(data: authRegister):
    response = auth_service.register(data)
    return response