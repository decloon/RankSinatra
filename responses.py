from data import collection
def get_response(user_input: str) -> str:
    
    if user_input == '!leaderboard':
        users = list(collection.find().sort('points', -1).limit(10))
        
        if not users:
            return "No users in leaderboard"
        
        leaderboard_message = "Leaderboard:\n"
        for user in users:
            member = user['user_id']
            name = member.display_name if member else "Unknown"
            points = user['points']
            leaderboard_message += f"{name}: {points} points\n"
            return f'{leaderboard_message}'
    elif user_input == '!challenge':
        pass

    if user_input[0] == "!":
        return "nothing"

    else:
        return 