from mongo import users_collection
from mongo import ask_question , get_random_question 
import discord
import utils

def handle_leaderboard_query():
    users = list(users_collection.find().sort('points', -1).limit(10))
    
    if not users:
        return "No users in leaderboard"
    
    leaderboard_message = "Leaderboard:\n"
    for user in users:
        member = user['user_id']
        points = user['points']
        leaderboard_message += f"{member}: {points} points\n"
    
    return f'{leaderboard_message}'
    
def handle_question_query():
    print("yall pretend like this is a question")
    random_question = get_random_question()
    print(random_question)
    question_text = random_question['questions']
    choices = random_question['choices']
    correct_answer = random_question['correct_answer']
    
    
    return f'{question_text}: {choices}; {correct_answer}'