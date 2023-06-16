from sqlalchemy.orm import Session
from . import models, schemas

def get_one(db: Session, id: int):
    return db.query(models.Group).filter(models.Group.id == id).first()

def get_by_name(db: Session, name: str):
    return db.query(models.Group).filter(models.Group.name == name).first()

def get_lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Group).offset(skip).limit(limit).all()

def create(db: Session, group: schemas.GroupCreate):
    entity = models.Group(**group.dict())
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity

def update(db: Session, db_entity:models.Group, updates: schemas.GroupUpdate):
    update_data = updates.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_entity, key, value)
    db.commit()
    return db_entity

def delete(db: Session, id: int):
    return db.query(models.Group).filter(models.Group.id == id).delete()