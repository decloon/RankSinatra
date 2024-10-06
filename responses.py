from data import users_collection
from data import ask_question , get_random_question 

def get_response(user_input: str) -> str:
    
    if user_input == '!leaderboard':
        users = list(users_collection.find().sort('points', -1).limit(10))
        
        if not users:
            return "No users in leaderboard"
        
        leaderboard_message = "Leaderboard:\n"
        for user in users:
            member = user['user_id']
            points = user['points']
            leaderboard_message += f"{member}: {points} points\n"
            return f'{leaderboard_message}'
        
    elif user_input == '!question':
        random = get_random_question()
        mine = ask_question(random)
        return f'{mine}'
        

    if user_input[0] == "!":
        return "nothing"

    else:
        return
def get_answer(user_input: str) -> str:
    ans = get_ans_data()
    return f'{ans}'