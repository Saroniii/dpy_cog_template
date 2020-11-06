# coding: UTF-8
import discord
from discord.ext import commands
import os
import pathlib
from utils import cog_loader as loader

TOKEN = os.environ['TOKEN']
command_prefix = ['!'] #コマンド接頭辞

class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.ready_check = False  # 重複してon_readyが呼び出されるのを回避するための変数
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
            print('既に起動処理は完了しています！')


intent: discord.Intents = discord.Intents.default()
bot = MyBot(command_prefix=command_prefix, intent=intent)

bot.run(TOKEN)
