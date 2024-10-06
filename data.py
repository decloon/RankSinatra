from pymongo import MongoClient
import os
uri = os.getenv("CONNECTION_STRING")

client = MongoClient('mongodb://localhost:27017/')
db = client.RankSinatra
collection = db.users

try:
    client.admin.command('ping')

    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)