import discord
from discord.ext import commands

class MyBot(commands.Bot):
    async def on_ready(self):
        activity = discord.Game(name='진예투')
        await self.change_presence(activity=activity)
        print('봇 시작!')

