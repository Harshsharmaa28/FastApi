from fastapi import FastAPI
from .config import connect_db
from .routes import user, auth, data

#Intialized the app
app = FastAPI()

# Connect to the database
connect_db()

# Include routes
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(data.router, prefix="/data", tags=["Data"])