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
        channel = discord.utils.find(
            lambda chnl: chnl.name == 'bot', guild.channels)
        break

    name = member.display_name
    source = before.channel.name if before.channel is not None else 'Disconnected'
    destination = after.channel.name if after.channel is not None else 'Disconnected'

    if source != destination:
        message = await channel.send(f'{name} moved from {source} to {destination}', tts=True)
        await message.delete(delay=10.0)
    else:
        # The action was a change in mute/deafen status
        pass


client.run(TOKEN)
