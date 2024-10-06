from typing import final
import os
import signal
from dotenv import load_dotenv
from discord import Intents, Client, Message, Member
from command_handlers import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)
channel_id = 1292397500824555593

# Prevents bot from responding to itself
@client.event
async def on_message(message) -> None:
    if message.author == client.user:
        return

    username = str(message.author)
    usermessage = message.content
    channel = await message.guild.fetch_channel(channel_id)

    # Ensure the message is in the correct channel
    if message.channel != channel:
        return

    print(f'[{channel}] {username}: {usermessage}')
    await send_message(message, usermessage, channel)

# Function to handle sending messages and processing challenges
async def send_message(message: Message, usermessage: str, channel) -> None:
    # # Check if the message is a command to create a challenge
    # if usermessage.startswith('!create_challenge'):
    #     # Logic to create a challenge
    #     pass
    # # Check if the message is a command to participate in a challenge
    # elif usermessage.startswith('!participate'):
    #     # Logic to participate in a challenge
    #     pass
    # # Check if the message is an answer to a challenge
    # elif usermessage.startswith('!answer'):
    #     # Logic to grade the answer and award points
    #     pass
    
    if usermessage == '!leaderboard':
        return handle_leaderboard_query()
        
    elif usermessage == '!question':
        return handle_question_query()
        

    if usermessage[0] == "!":
        return "nothing"

# Signal handler to gracefully shutdown the bot
def signal_handler(signal, frame):
    print("Shutting down...")
    client.close()

# Main function to run the bot
def main() -> None:
    signal.signal(signal.SIGINT, signal_handler)
    client.run(TOKEN)

if __name__ == '__main__':
    main()