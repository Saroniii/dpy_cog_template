import discord
from discord.ext import commands
import traceback
import re


class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def goodmorning(self, ctx :commands.Context):
        return await ctx.send('Good Morning')

def setup(bot):
    bot.add_cog(Cog(bot))
