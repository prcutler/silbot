import os
import random
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
import youtube_dl
from os import system
from discord import FFmpegPCMAudio
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

queue_list = []


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


@bot.command(name="ping", help='Check your ping')
async def ping(ctx):
    await ctx.send(f"Your ping is: {round(bot.latency * 1000)}ms.  I don't know if that is good or bad, so deal "
                   f"with it")


@bot.command(pass_context=True, brief="Make Silbot join the voice channel")
async def join(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("What the what?")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await voice.disconnect()
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.send(f"I get to play with the big kids! Joined '{channel}' channel")


@bot.command(pass_context=True, brief="Make Silbot leave the voice channel", aliases=['quit'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send("See ya, wouldn't wanna be ya!")
    else:
        await ctx.send("I don't want to talk to myself!")


@bot.command(pass_context=True, brief="Makes DJ Silbot play a song !play [url]")
async def play(ctx, url: str):

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except Exception:
        await ctx.send("Oops, you did it again!")
        return
    await ctx.send("Now Playing: " + url)
    voice = get(bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    voice.play(discord.FFmpegPCMAudio)
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()


@bot.command(pass_context=True, brief="Change the volume")
async def volume(ctx, volume):
    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.volume = volume
    await ctx.send("Pump it up! Volume: " + volume)

bot.run(TOKEN)