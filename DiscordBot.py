import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import csv

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
	print("Bot is ready dude!")

@client.event
async def on_message(message):
	if message.content.upper().startswith('!PING'):
		userId = message.author.id
		await client.send_message(message.channel, "<@%s> Pong!" % (userId))
	if message.content.upper().startswith('!SAY'):
		args = message.content.split(" ")
		await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
	if message.content.upper().startswith('!RANDOM'):
		args = message.content.split(" ")
		userId = message.author.id
		returnstr = str(random.randint(int(args[1]),int(args[2])))
		answer = "<@%s> Your Number is: " % (userId)
		await client.send_message(message.channel, answer+ returnstr)
	if message.content.upper().startswith('!JOKE'):
		jokes = []
		with open("jokes.csv") as csvfile:
			reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
			for row in reader: # each row is a list
				jokes.append(row)

		joke = random.randint(0,len(jokes))
		print(jokes)
		await client.send_message(message.channel, jokes[joke])


client.run("NDg4NDIyODI2NzYwNzMyNjc0.DncBEA.k56Y8gsRnXcpgbr08eQRngsnbaE")

"""if message.content == "shark":
	"	await client.send_message(message.channel, ":cookie:")"""