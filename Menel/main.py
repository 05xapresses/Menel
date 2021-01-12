import os

from dotenv import load_dotenv

from handlers import connect, guild_join, guild_remove, message, ready, shard_connect
from objects.bot import bot
from setup.import_commands import import_commands
from setup.setup_cliffs import setup_cliffs


load_dotenv()

cliffs = setup_cliffs()
import_commands(cliffs)

connect.setup(bot)
shard_connect.setup(bot)
ready.setup(bot)
message.setup(bot, cliffs)
guild_join.setup(bot)
guild_remove.setup(bot)

bot.run(os.getenv('DISCORD_TOKEN'), bot=True)