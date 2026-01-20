from sqlalchemy.orm import Session

from .. import models
from .. import schemas
<<<<<<< HEAD

def get_users(db: Session, response_model=list[schemas.user]):
    return db.query(models.user).all()

def get_user(db: Session, user_id:int):
    return db.query(models.user).filter(models.user.id == user_id).first()

def create_user(db:Session, user: schemas.userCreate):
    db_user = models.user(**user.model_dump())
=======
from ..auth import verify_password, hash_password

def get_users(db: Session, response_model=list[schemas.User]):
    return db.query(models.User).all()

def get_user(db: Session, user_id:int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db:Session, user: schemas.UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password = hashed_pw
    )
    
>>>>>>> 4d8fd5c2f41a8fa742aaef141cf113e941c0a1fb
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db:Session, user_id:int):
<<<<<<< HEAD
    user = db.query(models.user).filter(models.user.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
=======
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user


def authenticate_user(db: Session, username:str, password:str):
    user = db.query(models.User).filter(models.User.username, user.hashed_password)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
>>>>>>> 4d8fd5c2f41a8fa742aaef141cf113e941c0a1fb
    return user