from typing import final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, Member
from discord.ext import commands
from responses import get_response
from data import users_collection

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)
channel_id = 1292397500824555593

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command('add_points')
async def add_points(ctx, member: Member, points: int):
    """Add points to a user."""
    # Update the user's points in the database
    users_collection.update_one(
        {'user_id': member.id},
        {'$inc': {'points': points}},
        upsert=True
    )
    await ctx.send(f'Added {points} points to {member.display_name}.')

async def send_message(message: Message, user_message: str, channel: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled)')
        return

    user_message = user_message
    # if user_message == "a" or user_message == "b" or user_message == "c":
        

    try:
        response: str = get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)


#Prevents bot from responding to itself
@client.event
async def on_message(message) -> None:
    if message.author == client.user:
        return

    username = str(message.author)
    usermessage = message.content
    channel = await message.guild.fetch_channel(channel_id)


    if message.channel != channel:
        return

    print(f'[{channel}] {username}: {usermessage}')
    await send_message(message, usermessage, channel)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()