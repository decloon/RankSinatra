from mongo import users_collection
from mongo import ask_question , get_random_question 
    
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
        random = get_random_question()
        mine = ask_question(random)
        return f'{mine}'