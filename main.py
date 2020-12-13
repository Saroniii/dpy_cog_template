# coding: UTF-8
import discord
from discord.ext import commands
import os
import pathlib

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
            cur = pathlib.Path('.')

            for p in cur.glob(f"{folder_name}/*.py"):

                try:
                    print(f'cogs.{p.stem}', end="　")
                    bot.load_extension(f'cogs.{p.stem}')
                    print(f'success')

                except commands.errors.NoEntryPointError:
                    print(f'module.{p.stem}')

            self.ready_check = True
        
        else:
            print('The start up process is already complete!')


intent: discord.Intents = discord.Intents.default()
bot = MyBot(command_prefix=command_prefix, intents=intent)

bot.run(TOKEN)
