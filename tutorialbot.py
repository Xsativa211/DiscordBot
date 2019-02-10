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
    await client.change_presence(game=Game(name='My Own Feelings'))
    print('Working na po') 


@client.event
async def on_message(message):
    if message.content == 'g!':
        await client.send_message(message.channel,'Syempre ahh!')

@client.event
async def on_message(message):
    if message.content == '!g!2':
        await client.send_message(message.channel,'@forallpeople03#1592, Hello sa iyo!')

@client.event
async def on_message(message):
    if message.content == '!g!3':
        await client.send_message(message.channel,'tol, I don’t know what the FUCK you did. Sumisigaw yung anak ko sa taas, “Daddy! Daddy! Daddy!” Sabi ko, “Anak, bakit?” HAH? “Si tito Pker hindi ko alam nakatayo nalang jan hawak hawak yung kamay ko."')
        
        
client.run(str(os.environ.get('TOKEN')))
