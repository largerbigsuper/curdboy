
from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from apps.auth.schemas import User
from apps.security.utils import get_current_active_user
from database.db import get_db

from .utils import (ACCESS_TOKEN_EXPIRE_MINUTES, Token, authenticate_user,
                    create_access_token, user_password_change, user_signup, verify_password)

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
    return user_signup(db=db, user=user)


@router.post("/password_change/", response_model=User)
def password_change(payload: schemas.UserPasswordChange, 
                    current_user: Annotated[User, Depends(get_current_active_user)], 
                    db: Session = Depends(get_db)):
    # check old password
    if not verify_password(payload.password, current_user.password):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="error old password")
    
    return user_password_change(db, current_user.username, payload.new_password)

CODE_DICT = {
    "admin": "888888" 
}

@router.post("/password_reset/", response_model=User)
def password_reset(payload: schemas.UserPasswordReset, db: Session = Depends(get_db)):
    correct_code = CODE_DICT.get(payload.username)
    if not correct_code or payload.code != correct_code:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="error code")
    return user_password_change(db, payload.username, payload.password)


@router.get("/me/", response_model=User)
def get_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user

