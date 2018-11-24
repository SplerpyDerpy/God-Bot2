import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import json
from discord import Game
import emoji
import os


Client = discord.Client()
client = commands.Bot (command_prefix = "please")

@client.event
async def on_ready():
    print("ready")
    await client.change_presence(game=Game(name="with Jesus"))

@client.event
async def on_message(message):
    s = message.author.id
    if s == '401940988106375179':
        await client.delete_message(message)
        for i in range(10):
            await client.send_message(message.author, "@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257@God of Emu#7257")

        


client.run(os.getenv('TOKEN'))


