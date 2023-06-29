
from typing import Mapping

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from apps.auth import service
from database.db import get_db


def valid_user_id(user_id: int, db: Session = Depends(get_db)) -> Mapping:
    user =  service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    return user

def valid_group_id(group_id: int, db: Session = Depends(get_db)) -> Mapping:
    group = service.get_group_by_id(db, group_id)
    if not group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    return group

