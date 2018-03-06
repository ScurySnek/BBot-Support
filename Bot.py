import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
x = 1

chat_filter = ["BBGAY", "BBDICK", "BBMEN", "BBFUTA"]
bypass_list = ["262294923607277569"]
chat_filter_secret = ["ZXC"]



@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):


    
    if message.content == "sun":
        await client.send_message(message.channel, ":sunglasses:")

    if message.content.upper().startswith('!SPAM'):
        if message.author.id == "262294923607277569":
            x = 1
            args = message.content.split(" ")
            while x == 1:
                await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "fuck off, only DANMONEY can spam")
    
    

    if message.content.upper().startswith('!STOP'):
        if message.author.id == "262294923607277569":
            x = 10
            await client.send_message(message.channel, "Spam Stopped")
        
        else:
            await client.send_message(message.channel, "fuck off, only DANMONEY can stop the spam")

    contents=message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                await client.delete_message(message)
                await client.send_message(message.channel, "**Hey!** Only DANMONEY look at gay shit without being judged")
            
    
    
    for word in contents:
        if word.upper() in chat_filter_secret:
            await client.delete_message(message)
    
    if message.content.upper().startswith('!HELP'):
        await client.send_message(message.channel, """
    Hi, I am the kool bot and here are some commands:
    !ping to find out if I am online
    !amisupergay to see if you are an admin
    !say to have me repeat something
    !spam [message] Have me spam a message(in development)
    !stop to have me stop spamming
    bbneko z.x.c without the peroids to look at nekos in secret ;)
    I will call you out if you look for gay shit using the b bot.
    """)
        
        
    if message.content.upper() == "BBGAY":
        await client.send_message(message.channel, "miss me with that gay shit")


    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))

    if message.content.upper().startswith('!SAY'):
        if message.author.id == "262294923607277569":
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "fuck off, u arent danmoney")
    if message.content.upper().startswith('!AMISUPERGAY'):
        if "420481161727311892" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, "You are SUPER GAY")
        else:
            await client.send_message(message.channel, "no u")



client.run("NDIwNDcyNjQzNTk5NDY2NTA2.DX_xzw.3nUG3mlhXAo5TyOF3wBko7STvL0")
