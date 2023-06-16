from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.db import get_db

from . import schemas, service

router = APIRouter()

@router.post("/", response_model=schemas.Group)
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
    db_entity = service.get_by_name(db, name=group.name)
    if db_entity:
        raise HTTPException(status_code=400, detail="username already registered")
    return service.create(db=db, group=group)


@router.get("/", response_model=list[schemas.Group])
def read_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    entities = service.get_lists(db, skip=skip, limit=limit)
    return entities

@router.get("/{id}", response_model=schemas.Group)
def read_group(id: int, db: Session = Depends(get_db)):
    db_user = service.get_one(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{id}")
def delete_group(id: int, db: Session = Depends(get_db)):
    db_user = service.get_one(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    service.delete(db, id=id)

@router.put("/{id}", response_model=schemas.Group)
def update_group(id: int, group: schemas.GroupUpdate, db: Session = Depends(get_db)):
    db_entity = service.get_one(db, id=id)
    if db_entity is None:
        raise HTTPException(status_code=404, detail="User not found")
    return service.update(db, db_entity=db_entity, updates=group)
