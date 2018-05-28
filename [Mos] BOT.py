import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = '<')
chat_filter = ['FUCK', 'SHIT', 'BASTARD', 'NIGGER', 'ASS', 'CUNT', 'COCK', 'TWAT', 'WHORE', 'SLUT', 'DICK', 'FUCKED', 'FUCKING']

@client.event
async def on_ready():
    print('Bot is ready!')

@client.event
async def on_message(message):
    contents = message.content.split(' ')
    for word in contents:
        if word.upper() in chat_filter:
            await client.delete_message(message)
            await client.send_message(message.channel, '\t {} you\'re not allowed to use that word here.'.format(message.author))
        



client.run('NDUwNDAyNDIyMTI5Njg4NTc2.Dey2_Q.-LQ7kWm_xGfwb7hDMGV9IRLx78w')
