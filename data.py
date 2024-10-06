from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi    
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv()
uri = os.getenv("CONNECTION_STRING")

client = MongoClient(uri, server_api =ServerApi('1'))


db = client.RankSinatra


users_collection = db.users  # Collection for users
questions_collection = db.questions  # Collection for questions

try:
    client.admin.command('ping')

    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

def get_all_names():
    users = []
    cursor = users_collection.find({}, {"_id": 0, "user_id": 1})  # Exclude _id field, include only name field
    for document in cursor:
        users.append(document["user_id"])
    print (users)
    # return users

def get_all_questions():
    questions = []
    cursor = questions_collection.find({}, {"_id": 0, "questions": 1})  # Example field: question_text
    for document in cursor:
        questions.append(document["questions"])
    print(questions)
    # return questions


# Function to fetch a random question from the questions collection
def get_random_question():
    # Using aggregation with $sample to fetch one random document
    random_question = questions_collection.aggregate([{"$sample": {"size": 1}}])
    
    # The result is an iterable, so we need to retrieve the first (and only) item
    return next(random_question, None)
def ask_question():
    question_doc = get_random_question()  # Fetch a random question

    if question_doc:
        # Display the question and choices
        print(f"Question: {question_doc['questions']}")
        print("Choices:")
        for key, value in question_doc['choices'].items():
            print(f"{key}: {value}")

        # Get the user's answer
        user_answer = input("Please enter your answer (a, b, c): ").lower()

        # Check if the answer matches the correct answer
        correct_answer = question_doc['answers']
        if user_answer == correct_answer:
            print("Correct answer!")
            # Add a point to the user's score
        else:
            print("Incorrect answer.")
    else:
        print("No questions available.")

        
def main():
    # get_all_names()
    # get_all_questions()
    ask_question()

    
if __name__=='__main__':
    main()