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
    print(f"[bot.py] I am logged in as {config.botName} my owners id is {config.bot_ownerID} there name is {config.bot_owner_name} the date today is {today}")
    await load_db()

async def load_db():
    async with aiosqlite.connect("./data/main.db") as db:
        async with db.cursor() as cursor:
            try:
                await cursor.execute("SELECT * FROM users")
            except OperationalError as oe:
                print(f"Error has happend! {oe}")
        await db.commit()

@client.command()
async def load(ctx, extension):
    if ctx.author.id == config.bot_ownerID:
        client.load_extension(f'cogs.{extension}')
        embed = nextcord.Embed(title="Cog")
        embed.set_footer(text=f"Cog {extension} has been loaded!")
        await ctx.sen(embed=embed)
    else:
        await ctx.send(f"You can't run this command only {config.bot_owner_name} with the user id of {config.bot_ownerID}")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f"[bot.py] Successfully loaded cog\n\n{filename[:-3]}\n\n")
    else:
        print(f"[bot.py] Error loading cog\n\n{filename[:-3]}\n\n")
client.run(config.token)
