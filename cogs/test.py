from discord.ext import commands


class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def goodmorning(self, ctx: commands.Context):
        return await ctx.send('Good Morning')


async def setup(bot):
    await bot.add_cog(Cog(bot))
