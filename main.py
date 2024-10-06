from typing import final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

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