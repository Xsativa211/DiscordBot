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
    print('Working na po') 
    
@client.event
async def on_message(message):
    if message.content == 'levie':
        await client.send_message(message.channel,'tol, I don’t know what the FUCK you did. Sumisigaw yung anak ko sa taas, “Daddy! Daddy! Daddy!” Sabi ko, “Anak, bakit?” HAH? “Si tito Pker hindi ko alam nakatayo nalang jan hawak hawak yung kamay ko."')
    if ('levie') in message.content:
       await client.delete_message(message)    
    if message.content == 'Levie':
       await client.send_message(message.channel,'tol, I don’t know what the FUCK you did. Sumisigaw yung anak ko sa taas, “Daddy! Daddy! Daddy!” Sabi ko, “Anak, bakit?” HAH? “Si tito Pker hindi ko alam nakatayo nalang jan hawak hawak yung kamay ko."')
    if ('Levie') in message.content:
       await client.delete_message(message)     
    
    if message.content == 'Inviation':
       await client.send_message(message.channel,'Hello maspinadali na ang pagiinvite sa ating Discord server Group!')
       await client.send_message(message.channel,'Icopy paste lamang ito sa inyong browser https://discord.me/genocidero')
       await client.send_message(message.channel,'O kaya sabihin ninyo lang na discord.me/genocidero ')
    if message.content == 'inviation':
       await client.send_message(message.channel,'Hello maspinadali na ang pagiinvite sa ating Discord server Group!')
       await client.send_message(message.channel,'Icopy paste lamang ito sa inyong browser https://discord.me/genocidero')
       await client.send_message(message.channel,'O kaya sabihin ninyo lang na discord.me/genocidero ')
    
    
client.run(str(os.environ.get('TOKEN')))
