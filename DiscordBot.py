import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import csv

jokes = ["I just deleted all the German names off my phone. Its Hans free",
"Kim Kardashian is saddled with a huge arse but enough about Kanye West",
"Surely every car is a people carrier?",
"What's the difference between a 'hippo' and a 'Zippo'? One is really heavy the other is a little lighter",
"If I could take just one thing to a desert island I probably wouldn't go",
"Jesus fed 5000 people with two fishes and a loaf of bread. That's not a miracle. That's tapas",
"Red sky at night. Shepherd's delight. Blue sky at night.  Day",
"The first time I met my wife I knew she was a keeper.  She was wearing massive gloves",
"Clowns divorce. Custardy battle",
"They're always telling me to live my dreams. But I don't want to be naked in an exam I haven't revised for",
"I've decided to sell my Hoover... well it was just collecting dust.",
"I've written a joke about a fat badger but I couldn't fit it into my set.",
"Always leave them wanting more my uncle used to say to me. Which is why he lost his job in disaster relief.",
"I was given some Sudoku toilet paper. It didn't work. You could only fill it in with number ones and number twos.",
"I wanted to do a show about feminism. But my husband wouldn't let me.",
"Money can't buy you happiness? Well check this out I bought myself a Happy Meal.",
"Scotland had oil but it's running out thanks to all that deep frying.",
"I've been married for 10 years I haven't made a decision for seven.",
"This show is about perception and perspective. But it depends how you look at it.",
"I've written a joke about a fat badger but I couldn't fit it into my set",
"I heard a rumour that Cadbury is bringing out an oriental chocolate bar. Could be a Chinese Wispa.",
"I used to work in a shoe-recycling shop. It was sole-destroying.",
"I'm in a same-sex marriage... the sex is always the same.",
"My friend told me he was going to a fancy dress party as an Italian island. I said to him 'Don't be Sicily'.",
"I can give you the cause of anaphylactic shock in a nutshell.",
"The Pope is a lot like Doctor Who. He never dies just keeps being replaced by white men.",
"You know you are fat when you hug a child and it gets lost.",
"The universe implodes. No matter.",
"I was adopted at birth and have never met my mum. That makes it very difficult to enjoy any lapdance.",
"The good thing about lending someone your time machine is that you basically get it back immediately.",
"You know who really gives kids a bad name? Posh and Becks",
"Last night me and my girlfriend watched three DVDs back to back. Luckily I was the one facing the telly.",
"I was raised as an only child which really annoyed my sister.",
"You know you're working class when your TV is bigger than your book case.",
"I'm good friends with 25 letters of the alphabet... I don't know Y.",
"I took part in the sun tanning Olympics - I just got Bronze.",
"Pornography is often frowned upon but that's only because I'm concentrating.",
"I saw a documentary on how ships are kept together.  Riveting!",
"I waited an hour for my starter so I complained: 'It's not rocket salad.",
"My mum's so pessimistic that if there was an Olympics for pessimism... she wouldn't fancy her chances.",
"I needed a password eight characters long so I picked Snow White and the Seven Dwarves.",
"Crime in multi-storey car parks. That is wrong on so many different levels.",
"People say 'I'm taking it one day at a time'. You know what? So is everybody. That's how time works.",
"Drive-Thru McDonalds was more expensive than I thought...  once you've hired the car",
"I was playing chess with my friend and he said 'Let's make this interesting'. So we stopped playing chess.",
"My mother told me you don't have to put anything in your mouth you don't want to. Then she made me eat broccoli which felt like double standards.",
"I was in a band which we called The Prevention because we hoped people would say we were better than The Cure.",
"Someone asked me recently - what would I rather give up food or sex. Neither! I'm not falling for that one again  wife",
"I admire these phone hackers. I think they have a lot of patience. I can't even be bothered to check my OWN voicemails.",
"My friend died doing what he loved ... Heroin.",
"I've just been on a once-in-a-lifetime holiday. I'll tell you what never again.",
"I'm currently dating a couple of anorexics. Two birds one stone",
"I picked up a hitch hiker. You've got to when you hit them.",
"I bought one of those anti-bullying wristbands when",
"As a kid I was made to walk the plank. We couldn't afford a dog.",
"Being an England supporter is like being the over-optimistic parents of the fat kid on sports day.",
"What do you call a kid with no arms and an eyepatch?  Names.",
"Dave drowned. So at the funeral we got him a wreath in the shape of a lifebelt. Well",
"For Vanessa Feltz it's what he would have wanted.",
"Wooden spoons are great. You can either use them to prepare food. Or life is like a box of chocolates: Empty.",
"Hedgehogs - why can't they just share the hedge? if you can't be bothered with that just write a number on one and walk into a pub",
"I was watching the London Marathon and saw one runner dressed as a chicken and another runner dressed as an egg. I thought: 'This could be interesting'.",
"I had my boobs measured and bought a new bra. Now I call them Joe Cocker and Jennifer Warnes because they're up where they belong.",
"I went on a girls' night out recently. The invitation said 'dress to kill'. I went as Rose West.",
"I'm sure wherever my dad is; he's looking down on us.  He's not dead",
"Going to Starbucks for coffee is like going to prison for sex. You know you're going to get it just very condescending.",
"To the people who've got iPhones: you just bought one but it's going to be rough.",
"A spa hotel? It's like a normal hotel you didn't invent it!",
"I've been reading the news about there being a civil war in Madagascar. Well only in reception there's a picture of a pebble.",
"I started so many fights at my school - I had that attention-deficit disorder. So I didn't finish a lot of them I've seen it six times and there isn't."]


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
		joke = random.randint(0,len(jokes)-1)
		await client.send_message(message.channel, jokes[joke])


client.run("NDg4NDIyODI2NzYwNzMyNjc0.DncBEA.k56Y8gsRnXcpgbr08eQRngsnbaE")

"""if message.content == "shark":
	"	await client.send_message(message.channel, ":cookie:")"""