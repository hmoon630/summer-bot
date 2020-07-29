from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 안녕(self, ctx):
        await ctx.send('안녕! :wave:')