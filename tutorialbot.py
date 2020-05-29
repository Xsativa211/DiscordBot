import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import requests
import os
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Ragnarok Online Mobile',))
    print('Codes are working perfectly fine! you may use it now!') 

@client.event
async def on_message(message):
    if message.content == 'Upvotes: ':
       await client.send_message(message.channel,'Me!, salamat soar')

    if message.content == 'Upvote Needed:':
       await client.send_message(message.channel,'Me!, salamat soar')
client.run(str(os.environ.get('Mjg1ODQzMTYzNTg1ODM5MTA3.Xns5wA.BO0SlutWyZB5sMOhOjIwIqyTXEc')))
