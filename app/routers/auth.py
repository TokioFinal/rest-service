from typing import Annotated

from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.auth import Token, authRegister, authBaseRegister
from app.clients import auth_service
from fastapi import APIRouter, Depends

router = APIRouter()

@router.post("/register", response_model=authBaseRegister)
def register(data: authRegister):
    print("inside auth router ################################################")
    response = auth_service.register(data)
    print("after client call ################################################")
    return response

@router.post("/login", response_model = Token)
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    response = auth_service.login(form_data.__dict__)
    return response
    