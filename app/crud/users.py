from sqlalchemy.orm import Session

from .. import models
from .. import schemas

def get_users(db: Session, response_model=list[schemas.user]):
    return db.query(models.user).all()

def get_user(db: Session, user_id:int):
    return db.query(models.user).filter(models.user.id == user_id).first()

def create_user(db:Session, user: schemas.userCreate):
    db_user = models.user(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db:Session, user_id:int):
    user = db.query(models.user).filter(models.user.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user