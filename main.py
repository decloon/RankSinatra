from typing import final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, Member
from discord.ext import commands
from responses import get_response
from pymongo import MongoClient

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

mongo = MongoClient('mongodb://localhost:27017/')
db = mongo['discord_leaderboard']
collection = db['leaderboard']

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def add_points(ctx, member: Member, points: int):
    """Add points to a user."""
    # Update the user's points in the database
    collection.update_one(
        {'user_id': member.id},
        {'$inc': {'points': points}},
        upsert=True
    )
    await ctx.send(f'Added {points} points to {member.display_name}.')

@bot.command()
async def leaderboard(ctx):
    """Display the leaderboard."""
    # Get all users and sort by points
    users = list(collection.find().sort('points', -1).limit(10))
    
    if not users:
        await ctx.send("No users in the leaderboard yet.")
        return
    
    leaderboard_message = "Leaderboard:\n"
    for user in users:
        member = ctx.guild.get_member(user['user_id'])
        name = member.display_name if member else "Unknown"
        points = user['points']
        leaderboard_message += f"{name}: {points} points\n"
    
    await ctx.send(leaderboard_message)


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled)')
        return

    is_private = user_message[0] == '?'

    if is_private:
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

#Prevents bot from responding to itself
@client.event
async def on_message(message) -> None:
    if message.author == client.user:
        return

    username = str(message.author)
    usermessage = message.content
    channel = message.channel

    print(f'[{channel}] {username}: {usermessage}')
    await send_message(message)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()