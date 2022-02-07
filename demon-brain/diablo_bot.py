import asyncio
import time
import asyncio
import discord
from discord.ext import commands,tasks
import os
from discord.voice_client import VoiceClient
from random import choice
import json
from pistonapi import PistonAPI
from terminal import terminal
from functions import *
from discord.utils import get

decisions = []
private_channel = []


piston=PistonAPI()
def get_prefix(client,message):
    with open('jsonFiles/prefixes.json', 'r') as f:
       prefixes=json.load(f)
    return prefixes[str(message.guild.id)]

client=commands.Bot(command_prefix=get_prefix,case_insensitive=True)

@client.event
async def on_guild_join(guild):
    with open('jsonFiles/prefixes.json', 'r') as f:
       prefixes=json.load(f)

    prefixes[str(guild.id)]='?'

    with open('jsonFiles/prefixes.json', 'w') as f:
        json.dump(prefixes,f)

@client.event
async def on_guild_remove(guild):
    with open('jsonFiles/prefixes.json', 'r') as f:
       prefixes=json.load(f)

    prefixes.pop(str(guild.id))

    with open('jsonFiles/prefixes.json', 'w') as f:
        json.dump(prefixes,f)

@client.command(name='changeprefix',help='this changes the prefix ... use 2 arguments')
async def changeprefix(ctx,prefix):
    with open('jsonFiles/prefixes.json', 'r') as f:
       prefixes=json.load(f)

    prefixes[str(ctx.guild.id)]= prefix

    with open('jsonFiles/prefixes.json', 'w') as f:
        json.dump(prefixes,f)

status = ['?help', 'valzkai ae', 'ennatha solla','ada poda']

@client.event
async def on_ready():
    change_status.start()
    print('otha ayya ready :)')

@client.event
async def on_message(message):

  if message.author==client.user:
    return

  if message.content.startswith('valzkai'):
    if str(message.author) =='akash k tesla#1113':
          await message.channel.send('ohh... akash ah avan epayum ae ipadi than')
    else:
        await message.channel.send('ivan oruthan valzkai ae valzkai ae nu katharikitu')

  if len(message.mentions)>=1:
      if message.mentions[0]==client.user:
        await message.channel.send('yenna da un prechanai')
        with open('jsonFiles/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        temp_pre=prefixes[str(message.guild.id)]
        await message.channel.send(f"enna command prefix theriyala ya intha '**{temp_pre}**' ithan athu")

  await client.process_commands(message)


@client.command(name='addstatus',help='addstatus ps..only akash can use this command')
async def addstatus(ctx,*,arg):
    if str(ctx.message.author)=='akash k tesla#1113':
        status.append(arg)
        await ctx.message.channel.send(status)
    else:
        await ctx.message.send('only the great akash can use this command')

#show the ping
@client.command(name='ping',help='this command shows the ping')
async def ping(ctx):
    await ctx.send(f'haha ping goes... {round(client.latency * 1000)}ms')


@client.command(name='delete',help='this helps to delete')
async def delete(ctx,arg1):
    no=int(arg1)+1
    await ctx.message.channel.purge(limit=no)

@client.command(name='run',help='this runs a python code')
async def run(ctx,*,arg):
    code=arg.replace("```","")
    aki=piston.execute(language='py',version='3.9',code=code)
    await ctx.message.channel.send(str(aki))

@client.command(name='object',help='ai karumam la object ah execute pannum')
async def object(ctx,*,arg):
    object_driver_state = object_ds(arg)
    await ctx.message.channel.send(str(derites(aki, object_driver_state.aki)))

@client.command(name='action',help= 'syntax: ?action [action name] [object name]')
async def action(ctx,arg1,arg2):
    driver = action_ds(arg1, arg2)
    await ctx.message.channel.send(driver.aki)
    await ctx.message.channel.send(driver.asi)
    await ctx.message.channel.send(driver.lsi)
    await ctx.message.channel.send(driver.lti)
    await ctx.message.channel.send(driver.sto)

@client.command(name='dn' ,help= 'syntax: ?action [action name] [object name] ')
async def dn(ctx,arg1,arg2):
    dec_ds = add_driver_state([object_ds(arg2), action_ds(arg1, arg2)])
    decisions.append(decision(dec_ds, arg1 + ' ' + arg2, 0))
@client.command(name='print_dn',help='prints the decisions')
async def print_dn(ctx):
    for i in range(len(decisions)):
        await ctx.message.channel.send(decisions[i].sentence)

@client.command(name='mkdn',help = 'makes decision ')
async def mkdn(ctx):
    final_decision = make_dec(decisions)
    await ctx.message.channel.send(final_decision.sentence)

@client.command(name='delete_dn_all',help='deletes all the decisions')
async def delete_dn_all(ctx):
    await ctx.message.channel.send('deleting all the decisions')
    decisions = []

@client.command(name= 'quit',help = 'quits the terminal')
async def quit(ctx):

    for i in range(3,0,-1):
        await ctx.message.channel.send('deleting channel in '+str(i))
        await asyncio.sleep(1)
    if ctx.message.channel in private_channel:
        await ctx.message.channel.delete()

@client.command(name='terminal',help = 'creates a private channel')
async def terminal(ctx):
    guild = ctx.guild
    member = ctx.author
    admin_role = get(guild.roles, name="Admin")
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True),
        admin_role: discord.PermissionOverwrite(read_messages=True)
    }
    channel = await guild.create_text_channel('terminal', overwrites=overwrites)
    private_channel.append(channel)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.MissingRequiredArgument):
        await ctx.send('thambi...arguments ah olunga paaru pa, help venu na use panniko')

    if isinstance(error,discord.ext.commands.CommandNotFound):
        with open('jsonFiles/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        temp_pre2=prefixes[str(ctx.guild.id)]
        await ctx.send(f'dei kiruku pundamone apdi oru command ae illa... theriyala na **{temp_pre2}help** use pannu da thumai')


#delay for the game stats to change
@tasks.loop(seconds=25)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))






client.run('ODQ0NTE1MDg5NDk4MjQzMDgy.YKTh9w.KaOay_UgezP5Fdyh4JUt5VgUy9E')