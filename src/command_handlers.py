from mongo import users_collection
from mongo import ask_question , get_random_question 
import discord
from discord.ext import commands
    
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
    
    async def send_question(ctx):
        def check(m):
            return m.author == ctx.author and m.content in choices
        
        await ctx.send(question_text)
        for choice in choices:
            await ctx.send(choice)
        
        try:
            msg = await bot.wait_for('message', check=check, timeout=60.0)
        except asyncio.TimeoutError:
            await ctx.send('Sorry, you took too long to respond.')
        else:
            if msg.content == correct_answer:
                ask_question(random_question)
                await ctx.send("Correct! You have selected the correct answer!")
            else:
                await ctx.send("Incorrect. Sorry, that's not the correct answer.")
    
    return send_question