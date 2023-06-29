from typing import Mapping

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from apps.auth.dependencies import valid_group_id, valid_user_id
from database.db import get_db

from . import schemas, service

router = APIRouter()

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = service.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")
    return service.create_user(db=db, user=user)


@router.get("/users/", response_model=list[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = service.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=schemas.User)
def get_user(user: Mapping = Depends(valid_user_id)):
    return user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), user: Mapping = Depends(valid_user_id)):
    service.delete_user_by_id(db, user_id=user_id)

@router.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db), db_user: Mapping = Depends(valid_user_id)):
    return service.update_user(db, db_user=db_user, updates=user)

## Groups

@router.post("/groups/", response_model=schemas.Group)
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
    db_entity = service.get_group_by_name(db, name=group.name)
    if db_entity:
        raise HTTPException(status_code=400, detail="username already registered")
    return service.create_group(db=db, group=group)


@router.get("/groups/", response_model=list[schemas.Group])
def get_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    groups = service.get_groups(db, skip=skip, limit=limit)
    return groups

@router.get("/groups/{group_id}", response_model=schemas.Group)
def get_group(group: Mapping = Depends(valid_group_id)):
    return group

@router.delete("/groups/{group_id}")
def delete_group(group_id: int, db: Session = Depends(get_db), group: Mapping = Depends(valid_group_id)):
    service.delete_group_by_id(db, id=group_id)

@router.put("/groups/{group_id}", response_model=schemas.Group)
def update_group(group: schemas.GroupUpdate, db: Session = Depends(get_db), db_entity: Mapping = Depends(valid_group_id)):
    return service.update_group(db, db_entity=db_entity, updates=group)
