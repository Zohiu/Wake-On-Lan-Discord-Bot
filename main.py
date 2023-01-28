import asyncio

import discord # Discord.py or the old Pycord.
from wakeonlan import send_magic_packet

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('start'):
        if message.author.id == 123456789: # Put your discord user ID here.
            await message.channel.send('Alright, should be starting up now.')
            send_magic_packet("00.00.00.00.00.00") # Put your PC mac address here
            await asyncio.sleep(5)
        else:
            await message.channel.send('Hey! Only *insert your name* is allowed to do this!!!.') # add your name here

print("Starting...")
client.run('TOKEN') # Your bot token.