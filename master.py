import discord
from discord.ext import commands
import os
import json

TOKEN = open("token.txt", "r").read()
client = commands.Bot(command_prefix = 'm!')

with open('cringe.json', 'r') as f:
    crng = json.load(f)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('<:SillyChamp:743612208059252855>'):  
        await message.channel.send('<:SillyChamp:743612208059252855>')
        
    await client.process_commands(message)
    
@client.command()
async def poggers(ctx):
    await ctx.send('<:PogU:742244756599603210>')
    
@client.command()
async def sayname(ctx, user:discord.User):
    await ctx.send(f"Your name is {user.mention}")

@client.command()
async def cringe(ctx, user:discord.User):
    if not user.id in crng:
        crng[user.id] = {}
        crng[user.id]['count'] = 0
        
    crng[user.id]['count'] += 1
    
    await ctx.send(f"{user.mention} is cringe! Cringe counter now at {crng[user.id]['count']}.")
    
    with open('cringe.json','w') as f:
        json.dump(crng,f)

client.run(TOKEN)
