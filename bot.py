import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    starwars_quotes = [
        'I have a bad feeling about this.',
        "I'd rather kiss a Wookie!",
        'I find your lack of faith disurbing.',
        'May the Force be with you.',
        'Do.  Or do not.  There is no try',
        'Fear is the path to the dark side. Fear leads to anger; anger leads to hate; hate leads to suffering. I sense much fear in you.',
        'Well, if droids could think, there’d be none of us here, would there?',
        'I’m just a simple man trying to make my way in the universe',
        'So this is how liberty dies. With thunderous applause.',
        'I am one with the Force. The Force is with me.',
    ]

    if message.content == 'starwars!':
        response = random.choice(starwars_quotes)
        await message.channel.send(response)


client.run(TOKEN)