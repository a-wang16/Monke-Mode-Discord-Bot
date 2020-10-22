import discord
from discord.ext import commands
import os
import json

TOKEN = open("token.txt", "r").read()
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("<:SillyChamp:743612208059252855>"):  
        await message.channel.send("<:SillyChamp:743612208059252855>")
        
        
    
client.run(TOKEN)
