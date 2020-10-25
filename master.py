import discord
from discord.ext import commands
import os
import json

TOKEN = open("token.txt", "r").read()
client = commands.Bot(command_prefix = 'm!')

with open('cringe.json', 'r') as f:
    try:
        crng = json.load(f)
    except ValueError:
        crng = {}
        crng['users'] = []

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name="the jungle"))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

#    if message.content.startswith('<:SillyChamp:743612208059252855>'):  
#        await message.channel.send('<:SillyChamp:743612208059252855>')
    await client.process_commands(message)
    
@client.command()
async def sayname(ctx, user:discord.User):
    await ctx.send(f"Your name is {user.mention}")

@client.command()
async def cringe(ctx, user:discord.User): 
    if not user.id == 768625454701346846:
        for getID in crng['users']:
            if getID['id'] == user.id:
                getID['count'] += 1
                await ctx.send(f"{user.mention} is cringe! Cringe counter now at {getID['count']}.")
                break
        else:
            crng['users'].append({'id': user.id, 'count': 1})
            await ctx.send(f"{user.mention} is cringe! Cringe counter now at 1.")
        
        with open('cringe.json','w') as f:
            json.dump(crng,f)
    else:
        await ctx.send('Fuck you.')

@client.command(aliases=['cringeList'])
async def cringelist(ctx):
    sorted_obj = dict(crng) 
    sorted_obj['users'] = sorted(crng['users'], key=lambda x : x['count'], reverse=True)
    crngPos = 1
    crngList = ' '
    for getID in sorted_obj['users']:
        idToName = int(getID['id'])
        uName = client.get_user(idToName).name
        crngList += f"{crngPos}. {uName} - {getID['count']}\n"
        crngPos += 1
    await ctx.send(crngList)
    with open('cringe.json','w') as f:
            json.dump(sorted_obj,f)

@client.command()
async def echo(ctx, *, arg):
    await ctx.send(arg)

client.run(TOKEN)
