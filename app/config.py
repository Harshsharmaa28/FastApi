from pymongo import MongoClient

def connect_db():
    global db
    #Please Note we can Also use mongodb Atlas Here i have used mongodb compass (database name is usersdatabaase)
    client = MongoClient("mongodb://localhost:27017/usersdatabaase")
    db = client["user_db"]

# Accessible database connection
db = None