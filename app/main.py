from fastapi import FastAPI
from .database import engine, Base
<<<<<<< HEAD
from .routes import users
=======
from .routes import jokes, users, login
>>>>>>> 4d8fd5c2f41a8fa742aaef141cf113e941c0a1fb


Base.metadata.create_all(bind=engine)

app = FastAPI()

<<<<<<< HEAD
app.include_router(users.router)
=======
app.include_router(jokes.router)
app.include_router(users.router)
app.include_router(login.router)
>>>>>>> 4d8fd5c2f41a8fa742aaef141cf113e941c0a1fb

@app.get("/")
def root():
    return {"message": "FastAPI CRUD app running!"}
