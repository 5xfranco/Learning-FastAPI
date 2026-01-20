from pydantic import BaseModel

<<<<<<< HEAD
class userBase(BaseModel):
    name: str
    email:str
    password: str

class userCreate(userBase):
    pass

class user(userBase):
    id: int

    class Config:
        from_attributes = True
=======
class UserBase(BaseModel):
    name: str
    email:str
    

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    hashed_password:str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email:str
    plain_text_password: str
>>>>>>> 4d8fd5c2f41a8fa742aaef141cf113e941c0a1fb
