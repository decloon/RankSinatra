from mongo import users_collection
from mongo import ask_question , get_random_question 
import discord
import utils
import json

class SimpleView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='Press me!', style=discord.ButtonStyle.primary)
    async def press_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.value = True
        await interaction.response.send_message('Button pressed!', ephemeral=True)
        self.stop()

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
    question = random_question['questions']
    choices = random_question['choices']
    correct_choice = random_question['answers']
    
    
    return question, choices, correct_choice