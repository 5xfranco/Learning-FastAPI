from pydantic import BaseModel

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