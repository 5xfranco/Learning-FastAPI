from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db



    finally:
        db.close()

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.get("/{user_id}", response_model=schemas.user)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)


@router.post("/", response_model=schemas.user)
def ceate_new_user(user: schemas.userCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@router.delete("/{user_id}", response_model=schemas.user)
def delete_user(user_id:int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)

