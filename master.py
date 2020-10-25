import discord
from discord.ext import commands
import os
import json

#   Pulls the token from set text file and defines a command prefix
TOKEN = open("token.txt", "r").read()
client = commands.Bot(command_prefix = 'm!')

#   Loads json files for commands
with open('cringe.json', 'r') as f:
    try:
        crng = json.load(f)
    except ValueError:
        crng = {}
        crng['users'] = []

#   Keep as a relic for future programming
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name="the jungle"))
    print('We have logged in as {0.user}'.format(client))

#   Reacts to user messages when they happen
@client.event
async def on_message(message):
    #   Prevents a self loop from bot messages
    if message.author == client.user:
        return
        
#   Keep as a relic for future programming
#   if message.content.startswith('<:SillyChamp:743612208059252855>'):  
#       await message.channel.send('<:SillyChamp:743612208059252855>')

    await client.process_commands(message)

#   Keep as a relic for future programming
#@client.command()
#async def sayname(ctx, user:discord.User):
#    await ctx.send(f"Your name is {user.mention}")

#Creates and adds a cringe counter for the user pinged
@client.command()
async def cringe(ctx, user:discord.User): 
    if not user.id == 768625454701346846:
        for getID in crng['users']:
            if getID['id'] == user.id:
                getID['count'] += 1
                await ctx.send(f"{user.name} is cringe! Cringe counter now at {getID['count']}.")
                if not getID['name'] == user.name:
                    getID['name'] = user.name
                break
        else:
            crng['users'].append({'id': user.id, 'count': 1,'name': user.name})
            await ctx.send(f"{user.name} is cringe! Cringe counter now at 1.")
        
        with open('cringe.json','w') as f:
            json.dump(crng,f)
    else:
        await ctx.send('Fuck you.')

#Sorts and messages the rank of the most cringe people
@client.command(aliases=['cringeList'])
async def cringelist(ctx):
    sorted_obj = dict(crng) 
    sorted_obj['users'] = sorted(crng['users'], key=lambda x : x['count'], reverse=True)
    crngPos = 1
    crngList = ' '
    for getID in sorted_obj['users']:
        idToName = int(getID['id'])
        uName = getID['name']
        crngList += f"{crngPos}. {uName} - {getID['count']}\n"
        crngPos += 1
    await ctx.send(crngList)
    with open('cringe.json','w') as f:
            json.dump(sorted_obj,f)

#Simple echo command to repeat the user's message
@client.command()
async def echo(ctx, *, arg):
    await ctx.send(arg)

#Connects the bot to the Discord API
client.run(TOKEN)
