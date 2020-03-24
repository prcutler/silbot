import os

import discord
from dotenv import load_dot_env

load_dot_env
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Dicord.")

client.run(TOKEN)