import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot (command_prefix = "please")

@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(message):
    if message.content.upper().startswith('SUCK MY DICK') or message.content.upper().startswith('FUCK YOU') or message.content.upper().startswith('GO FUCK YOURSELF'):
        await client.send_message(message.channel, "no, you")
    elif message.content.upper().startswith('GO'):
        args = message.content.split(" ")
        print(args[1:])
        if args[1:] == ['suck', 'a', 'dick'] or args[1:] == ['kill', 'yourself']:
            await client.send_message(message.channel, "no, you")
    elif message.content.upper().startswith('-RULE34') or message.content.upper().startswith('-HENTAI'):
        await client.send_message(message.channel, "Thilan stop")
    elif message.content.upper().startswith('FUCK'):
        await client.send_message(message.channel, "Stop Swearing")
    elif message.content.startswith('@EVERYONE'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> why are you pinging everyone so pointlessly?" % (userID))


        
        
    


client.run("NTAxMjU4MDYyNjg2OTc4MDU4.DqWwgQ.YYnODCk_YRpErNojzSgLJI1OV_0")
