from config import Config
from bot import MyBot
from cogs import Greetings

COGS_LIST = [Greetings]


if __name__ == '__main__':
    bot = MyBot(command_prefix='.')

    for cog in COGS_LIST:
        bot.add_cog(cog(bot))

    bot.run(Config.token)
