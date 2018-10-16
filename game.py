import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import json
from discord import Game

Client = discord.Client()
client = commands.Bot (command_prefix = "please")

@client.event
async def on_ready():
    print("ready")
    await client.change_presence(game=Game(name="with Jesus"))

@client.event
async def on_message(message):

    if message.content.upper().startswith('GO'):
        args = message.content.split(" ")
        print(args[1:])
        if args[1:] == ['suck', 'a', 'dick'] or args[1:] == ['kill', 'yourself']:
            await client.send_message(message.channel, "no, you")
    elif message.content.upper().startswith('-RULE34') or message.content.upper().startswith('-HENTAI'):
        await client.send_message(message.channel, "Thilan stop")
    args = message.content.split(" ")	
    for word in args:
        if word.upper() == '@EVERYONE':
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> why are you pinging everyone so pointlessly?" % (userID))
        print(word)
        if word.upper() == ("FUCK") or word.upper() == ("SHIT"): 		
            if message.content.upper().startswith('SUCK MY DICK') or message.content.upper().startswith('FUCK YOU') or message.content.upper().startswith('GO FUCK YOURSELF'):
                await client.send_message(message.channel, "no, you")
                break
            else:
                async for msg in client.logs_from(message.channel, 1):
                    await client.add_reaction(msg, '😠')
                break



client.run("NTAxMjU4MDYyNjg2OTc4MDU4.DqWwgQ.YYnODCk_YRpErNojzSgLJI1OV_0")

