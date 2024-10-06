from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi    
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv()
uri = os.getenv("CONNECTION_STRING")

client = MongoClient(uri, server_api =ServerApi('1'))


db = client.RankSinatra
collection = db.users

try:
    client.admin.command('ping')

    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# def get_all_names():
def main():
    users = []
    cursor = collection.find({}, {"_id": 0, "user_id": 1})  # Exclude _id field, include only name field
    for document in cursor:
        users.append(document["user_id"])
    print (users)

    
    # cursor = collection.find({})
    # for document in cursor:
    #     print(document)

if __name__=='__main__':
    main()