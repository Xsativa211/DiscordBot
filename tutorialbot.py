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
    if message.content == 'levie':
        await client.send_message(message.channel,'tol, I don’t know what the FUCK you did. Sumisigaw yung anak ko sa taas, “Daddy! Daddy! Daddy!” Sabi ko, “Anak, bakit?” HAH? “Si tito Pker hindi ko alam nakatayo nalang jan hawak hawak yung kamay ko."')
    if ('levie') in message.content:
       await client.delete_message(message)    
    if message.content == 'Levie':
       await client.send_message(message.channel,'tol, I don’t know what the FUCK you did. Sumisigaw yung anak ko sa taas, “Daddy! Daddy! Daddy!” Sabi ko, “Anak, bakit?” HAH? “Si tito Pker hindi ko alam nakatayo nalang jan hawak hawak yung kamay ko."')
    if ('Levie') in message.content:
       await client.delete_message(message)
    if message.content == '!link':
       await client.send_message(message.channel,'Discord Invitation link\nhttps://discord.me/GenocideGuild')
    if ('!link') in message.content:
       await client.delete_message(message)
    if message.content == '!Link':
       await client.send_message(message.channel,'Discord Invitation link \nhttps://discord.me/GenocideGuild')
    if ('!Link') in message.content:
       await client.delete_message(message)    
    if message.content == '!rules':
       await client.send_message(message.channel,':regional_indicator_r: :regional_indicator_u: :regional_indicator_l: :regional_indicator_e: :regional_indicator_s: \n1: respect OFFICERS and CoMembers\n\n2: bawal Mahiyain.\n\n3: GENDER EQUALITY lalo na may LGBT tayo dito sa guild.\n\n4: bawal din sapilitan nang hihingi ng tulong wait nyo maubos ang CT nila tutulungan din naman nila kayo.\n\n5: Wag Tawagin sa hindi panglan ang isang CoMember.\n\n6: kung meron ka isasali sa guild pasalihin mo muna sa DISCORD.\n\n7: bawal ang mayabang :)\n\n8: Share Knowledge ( dahil hindi ka naman mauubusan nyan ) tulungan mo ung iba.\n\n9: Always Check DISCORD for news and events.\n\n10: Wag ka masyado mag ADIK may BUHAY kapa sa LABAS ng RAGNAROK,. And Mag Enjoy lang tayo ')
    if ('!rules') in message.content:
       await client.delete_message(message)  
    if message.content == '!Rules':
       await client.send_message(message.channel,':regional_indicator_r: :regional_indicator_u: :regional_indicator_l: :regional_indicator_e: :regional_indicator_s: \n1: respect OFFICERS and CoMembers\n\n2: bawal Mahiyain.\n\n3: GENDER EQUALITY lalo na may LGBT tayo dito sa guild.\n\n4: bawal din sapilitan nang hihingi ng tulong wait nyo maubos ang CT nila tutulungan din naman nila kayo.\n\n5: Wag Tawagin sa hindi panglan ang isang CoMember.\n\n6: kung meron ka isasali sa guild pasalihin mo muna sa DISCORD.\n\n7: bawal ang mayabang :)\n\n8: Share Knowledge ( dahil hindi ka naman mauubusan nyan ) tulungan mo ung iba.\n\n9: Always Check DISCORD for news and events.\n\n10: Wag ka masyado mag ADIK may BUHAY kapa sa LABAS ng RAGNAROK,. And Mag Enjoy lang tayo ')
    if ('!Rules') in message.content:
       await client.delete_message(message)
    if message.content == '!status':
       await client.send_message(message.channel,'I am active do not worry!')
    if message.content == '!kafra':
        await client.send_message(message.channel,'To use Kafra Bot you must type \n `!db<space><itemname>!` for **example** `!db Poring` \n The bot will search through database with the name poring, and you have to choose a number which type of item you are looking for either \n 1 \n 2 \n 3 \n Simple as that :D')
    if message.content == '!Kafra':
        await client.send_message(message.channel,'To use Kafra Bot you must type \n `!db<space><itemname>!` for **example** `!db Poring` \n The bot will search through database with the name poring, and you have to choose a number which type of item you are looking for either \n 1 \n 2 \n 3 \n Simple as that :D')

    if message.content.startswith('!genocide'):
        output = message.content.replace('!genocide ', '')
        await client.send_message(message.channel, ' @here ' + output)    
 
    
    
client.run(str(os.environ.get('TOKEN')))
