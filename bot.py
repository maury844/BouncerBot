import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_voice_state_update(member, before, after):
    channel = None
    for guild in client.guilds:
        channel = discord.utils.find(lambda chnl: chnl.name == 'bot', guild.channels)
        break
    
    await channel.send(f'{before.channel.name} old, {after.channel.name} new')

    # await member.create_dm()
    # await member.dm_channel.send(
    #     f'Hi {member.name}, welcome to my Discord server {before}, {after}!'
    # )


client.run(TOKEN)