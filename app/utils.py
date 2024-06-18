import bcrypt
from .config import db

#Hashing Password using bcrypt
def get_password_hash(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

#Verifying password is correct or not
def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

#Finding user email
def get_user(email: str):
    return db.users.find_one({"email": email})