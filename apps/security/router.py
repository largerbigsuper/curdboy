
from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from apps.auth.schemas import User
from apps.security.utils import get_current_active_user
from database.db import get_db

from .utils import (ACCESS_TOKEN_EXPIRE_MINUTES, Token, authenticate_user,
                    create_access_token, signup_user)

from . import schemas

router = APIRouter()


@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/signup/", response_model=User)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return signup_user(db=db, user=user)


@router.get("/me/", response_model=User)
def get_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user

