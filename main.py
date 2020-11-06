# coding: UTF-8
import discord
from discord.ext import commands
import os
import pathlib
from utils import cog_loader as loader

TOKEN = os.environ['TOKEN']
command_prefix = ['!'] #Prefix

class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.ready_check = False  # Variable to prevent duplicate on_ready events from being triggered
        super().__init__(*args, **kwargs)

    async def on_ready(self):

        if self.ready_check == False:

            print('Logged in as')
            print(self.user.name)
            print(self.user.id)
            print(f'import')
            folder_name = 'cogs'
            loader().cog_load(self, f'{folder_name}/*.py')

            print('------')
            self.ready_check = True
        
        else:
            print('The start up process is already complete!')


intent: discord.Intents = discord.Intents.default()
bot = MyBot(command_prefix=command_prefix, intent=intent)

bot.run(TOKEN)
