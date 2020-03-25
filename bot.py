import os
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='starwars', help='Responds with a random Star Wars quote')
async def star_wars(ctx):

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

    response = random.choice(starwars_quotes)
    await ctx.send(response)


@bot.command(brief="Check my ping!")
async def ping(ctx):
    await ctx.send(f"Your ping is: {round(client.latency * 1000)}ms.  I don't know if that is good or bad, so deal "
                   f"with it")

bot.run(TOKEN)