import discord
from discord.ext import commands
import json
import os
import requests
import random
from replit import db
#my bot token
my_secret = os.environ['TOKEN']

#Bot logging on to it's account
client = commands.Bot(command_prefix = '$')

@client.event 
async def on_ready():
  print('Logged in as {0.user}'.format(client))
#quick command to get data from json
async def get_money_data():
  with open("money.json", "r") as f:
   users = json.load(f)
  return users
#balance command
@client.command()
async def balance(ctx):
  await open_account(ctx.author)
  #defining things for the embed
  users = await get_money_data()
  user = ctx.author
  wallet_amount = users[str(user.id)]["wallet"]
  #embed that will be sent when command is used
  em = discord.Embed(title = f"{ctx.author.name}'s balance", color = 420696)
  embed.add_field(name = 'Money', value = wallet_amount)
  await ctx.send(embed = em)
#command that will activate if user does not have data in json file
async def open_account(user):
  users = await get_money_data()
  if str(user.id) in users:
    return False
  else:
    users[str(user.id)]:["wallet"] = 0
  with open("money.json","w") as f:
    json.dump(users,f)
  return True
#command that will be sent whenever money will be added
async def add_money(amount, user):
  await open_account(user)
  amt = amount
  users = await get_money_data()
  users[str(user.id)]['wallet'] += amt
  with open("money.json", "w") as f:
    json.dump(users, f)

#a starting command for the bot
@client.command()
async def embed(ctx, user):
    user = ctx.author
    embed=discord.Embed(title="Welcome to Bot Name", description="You have just recieved:", color=420696)
    embed.add_field(name = '500 Money', value = 'and', inline = False)
    embed.add_field(name = 'A Free Low Tier Item', value = 'Use the $help command to see a list of useful commands', inline = False)
    embed.set_thumbnail(url="https://hatrabbits.com/wp-content/uploads/2017/01/random.jpg")
    await ctx.send(embed=embed)
    await open_account(ctx.author)
    await add_money(500, user)

#discord bot client
client.run(os.getenv('TOKEN'))
