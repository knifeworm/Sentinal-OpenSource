from sqlite3.dbapi2 import Error, OperationalError
import nextcord
from nextcord.ext import commands
import config
import aiosqlite
from datetime import date
today = date.today()
client = commands.Bot(command_prefix=config.token)

@client.event
async def on_ready():
    async with aiosqlite.connect("./data/main.db") as db:
        async with db.cursor() as cursor:
            await cursor.execute("CREATE TABLE IF NOT EXISTS users (userId INTEGER, guildId INTEGER)")
            await cursor.execute("CREATE TABLE IF NOT EXISTS guilds (guildId INTEGER)")
        await db.commit()
    print(f"I am logged in as {config.botName} my owners id is {config.bot_owner_id} there name is {config.bot_owner_name} the date today is {today}")
    await load_db()

async def load_db():
    async with aiosqlite.connect("./data/main.db") as db:
        async with db.cursor() as cursor:
            try:
                await cursor.execute("SELECT * FROM users")
            except OperationalError as oe:
                print(f"Error has happend! {oe}")
        await db.commit()


client.run(config.token)