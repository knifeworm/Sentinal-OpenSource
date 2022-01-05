from sqlite3.dbapi2 import Error, OperationalError
import nextcord
from nextcord.ext import commands
from nextcord.ext import ipc
import config
import aiosqlite
from datetime import date
import os
today = date.today()

class MyBot(commands.Bot):

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

        self.ipc = ipc.Server(self,secret_key= config.secret_key)

    async def on_ipc_ready(self):
        print("Ipc server is ready!")

    async def on_ipc_error(self, endpoint, error):
        print(endpoint, "raised", error)

    async def on_ready(self):
        async with aiosqlite.connect("./data/main.db") as db:
            async with db.cursor() as cursor:
                await cursor.execute("CREATE TABLE IF NOT EXISTS users (userId INTEGER, guildId INTEGER)")
                await cursor.execute("CREATE TABLE IF NOT EXISTS guilds (guildId INTEGER)")
            await db.commit()
        print(f"I am logged in as {config.botName} my owners id is {config.bot_ownerID} there name is {config.bot_owner_name} the date today is {today}")
        await load_db()


client = MyBot(command_prefix = config.prefix)

@client.ipc.route()
async def get_guild_count(data):
    return len(client.guilds)


@client.ipc.route()
async def get_guild_ids(data):
    final = []
    for guild in client.guilds:
        final.append(guild.id)
    return final

@client.ipc.route()
async def get_guild(data):
    guild = client.get_guild(data.guild_id)
    if guild is None: return None

    guild_data = {
        "name": guild.name,
        "id": guild.id,
        "prefix": config.prefix
    }

    return guild_data

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
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"You can't run this command only {config.bot_owner_name} with the user id of {config.bot_ownerID}")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f"Successfully loaded cog\n\n{filename[:-3]}\n\n")
    else:
        print(f"Error loading cog\n\n{filename[:-3]}\n\n")

client.ipc.start()
client.run(config.token)
