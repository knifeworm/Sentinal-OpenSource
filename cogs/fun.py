import nextcord
from nextcord.ext import commands
import config
from datetime import date
import aiohttp
today = date.today()

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            dogjson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/dog')
            factjson = await request2.json()
        embed = nextcord.Embed(title="Pictures | Dog",description=factjson['fact'],color=0x49FF2C)
        embed.set_image(url=dogjson['link'])
        embed.set_footer(text=f"Information requested by {ctx.author.display_name}", icon_url=f"{ctx.author.avatar}")
        print(f"[bot.py]Someone requested a picture of a dog! Woof! Woof!")
        await ctx.send(embed=embed)

    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat')
            catjson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/cat')
            factjson = await request2.json()

        embed = nextcord.Embed(title="Pictures | Cat", description=factjson['fact'], color=0x49FF2c)
        embed.set_image(url=catjson['link'])
        embed.set_footer(text=f"Information requested by {ctx.author.display_name}", icon_url=f"{ctx.author.avatar}")
        print(f"[bot.py]Someone requested a picture of a cat! Meow! Meow!")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(fun(client))