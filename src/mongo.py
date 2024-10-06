from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi    
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
uri = os.getenv("CONNECTION_STRING")

# Initialize MongoDB client
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.RankSinatra

# Collections
users_collection = db.users
questions_collection = db.questions

# Test connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

def get_all_names():
    """Fetch all user IDs from the users collection."""
    users = []
    cursor = users_collection.find({}, {"_id": 0, "user_id": 1})
    for document in cursor:
        users.append(document["user_id"])
    print(users)
    return users

def get_all_questions():
    """Fetch all questions from the questions collection."""
    questions = []
    cursor = questions_collection.find({}, {"_id": 0, "questions": 1})
    for document in cursor:
        questions.append(document["questions"])
    print(questions)
    return questions

def get_random_question():
    """Fetch a random question from the questions collection."""
    random_question = questions_collection.aggregate([{"$sample": {"size": 1}}])
    return next(random_question, None)

def ask_question(question_result):
    """Format a question and its choices for display."""
    if question_result:
        temp_quest = f"Question: {question_result['questions']}"
        choice = "Choices:"
        rar = []
        for key, value in question_result['choices'].items():
            rar.append(f"{key} {value}")
        return f'{temp_quest}\n{choice}\n' + '\n'.join(rar)
    return "No question available."

# Expose functions as part of the connection pool
__all__ = ['get_all_names', 'get_all_questions', 'get_random_question', 'ask_question']
