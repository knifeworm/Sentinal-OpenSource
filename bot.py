from sqlite3.dbapi2 import Error, OperationalError
import nextcord
from nextcord import file
from nextcord.ext import commands
import config
import aiosqlite
from datetime import date
import os
today = date.today()
client = commands.Bot(command_prefix=config.token)

@client.event
async def on_ready():
    async with aiosqlite.connect("./data/main.db") as db:
        async with db.cursor() as cursor:
            await cursor.execute("CREATE TABLE IF NOT EXISTS users (userId INTEGER, guildId INTEGER)")
            await cursor.execute("CREATE TABLE IF NOT EXISTS guilds (guildId INTEGER)")
        await db.commit()
    print(f"I am logged in as {config.botName} my owners id is {config.bot_ownerID} there name is {config.bot_owner_name} the date today is {today}")
    await load_db()

async def load_db():
    async with aiosqlite.connect("./data/main.db") as db:
        async with db.cursor() as cursor:
            try:
                await cursor.execute("SELECT * FROM users")
            except OperationalError as oe:
                print(f"Error has happend! {oe}")
        await db.commit()


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f"Successfully loaded cog\n\n{filename[:-3]}\n\n")
    else:
        print(f"Error loading cog\n\n{filename[:-3]}\n\n")
client.run(config.token)