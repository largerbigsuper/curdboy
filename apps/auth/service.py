from sqlalchemy.orm import Session

from database.db import get_db

from . import models, schemas


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users2(skip: int = 0, limit: int = 100):
    return next(get_db()).query(models.User).offset(skip).limit(limit).all()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, db_user:models.User, updates: schemas.UserUpdate):
    update_data = updates.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    return db_user

def delete_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).delete()


## Groups 
def get_group_by_id(db: Session, group_id: int):
    return db.query(models.Group).filter(models.Group.id == group_id).first()

def get_group_by_name(db: Session, name: str):
    return db.query(models.Group).filter(models.Group.name == name).first()

def get_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Group).offset(skip).limit(limit).all()

def create_group(db: Session, group: schemas.GroupCreate):
    entity = models.Group(**group.dict())
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity

def update_group(db: Session, db_entity:models.Group, updates: schemas.GroupUpdate):
    update_data = updates.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_entity, key, value)
    db.commit()
    return db_entity

def delete_group_by_id(db: Session, group_id: int):
    return db.query(models.Group).filter(models.Group.id == group_id).delete()