from sqlite3.dbapi2 import Error, OperationalError
import nextcord
from nextcord.ext import commands
from nextcord.ext import ipc
import config
import aiosqlite
from datetime import date
import os
import aiohttp
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

#Dog
@client.command()
async def dog(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog')
      dogjson = await request.json()
      request2 = await session.get('https://some-random-api.ml/facts/dog')
      factjson = await request2.json()

   embed = nextcord.Embed(title="Pictures | Dog",description=factjson['fact'],color=0x49FF2C)
   embed.set_image(url=dogjson['link'])
   embed.set_footer(text=f"Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url} {round(self.client.latency * 1000)}ms")
   print(f"[bot.py]Someone requested a picture of a dog! Woof! Woof!")
   await ctx.send(embed=embed)

#Cat
@client.command()
async def dog(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/animal/cat')
      dogjson = await request.json()
      request2 = await session.get('https://some-random-api.ml/facts/cat')
      factjson = await request2.json()

   embed = nextcord.Embed(title="Pictures | Cat",description=factjson['fact'],color=0x49FF2C)
   embed.set_image(url=dogjson['link'])
   embed.set_footer(text=f"Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url} {round(self.client.latency * 1000)}ms")
   print(f"[bot.py]Someone requested a picture of a cat! Meow.")
   await ctx.send(embed=embed)

client.ipc.start()
client.run(config.token)
