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

    return    next(random_question, None)
def ask_question(question_result):
    # question_doc = get_random_question()  # Fetch a random question
    bot_query = question_result['questions']
    
    if question_result:
        # Display the question and choices
        temp_quest = f"Question: {question_result['questions']}"
        choice = "Choices:"
        rar = []
        for key, value in question_result['choices'].items():
            rar.append(key)
            rar.append(value)
        
        return f'{temp_quest}\n{choice}\n{rar[0]} {rar[1]} \n{rar[2]} {rar[3]} \n{rar[4]} {rar[5]}'


    # return bot_query

# def get_ans_data(question_result):
#     user_answer = input("Please enter your answer (a, b, c): ").lower()

#         # Check if the answer matches the correct answer
#     correct_answer = question_result['answers']
#     if user_answer == correct_answer:
#         return("Correct answer!")
#         # Add a point to the user's score
#     else:
#         return "Incorrect answer." 
def main():
    # get_all_names()
    # get_all_questions()
    ask_question()

    
if __name__=='__main__':
    main()