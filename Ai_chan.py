import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
#Made by Sano
#login
bot = discord.Client()

#log in message
@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name)
    print("ID: " + bot.user.id)
    print('------')

#On event
@bot.event
async def on_message(message):
#command to say something i would say
    if message.content.lower() == "~love" :
        file = open('love_advice.txt', 'r+', encoding='utf-8', errors='ignore')
        wholeFile = file.readlines()
        RanLine = random.randrange(221) + 1
        print(RanLine)
        Line = wholeFile[RanLine]
        print(Line)
        await bot.send_message(message.channel,Line)
        file.close
                        
#run
bot.run("API TOKEN")
