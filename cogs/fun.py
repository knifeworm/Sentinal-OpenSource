#Imports
import nextcord
from nextcord.ext import commands
import config
from datetime import date
import aiohttp
today = date.today()

#Setup
class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

#Events

#Commands
    #Dog
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
        print(f"[fun.py]Someone requested a picture of a dog! Woof! Woof!")
        await ctx.send(embed=embed)

    #Cat
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
        print(f"[fun.py]Someone requested a picture of a cat! Meow! Meow!")
        await ctx.send(embed=embed)

    #Bird
    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/birb')
            birdjson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/bird')
            factjson = await request2.json()

        embed = nextcord.Embed(title="Pictures | Bird", description=factjson['fact'], color=0x49FF2c)
        embed.set_image(url=birdjson['link'])
        embed.set_footer(text=f"Information requested by {ctx.author.display_name}", icon_url=f"{ctx.author.avatar}")
        print(f"[fun.py]Someone requested a picture of a bird! *Bird noises*")
        await ctx.send(embed=embed)

        #Fox
        @commands.command()
        async def cat(self, ctx):
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://some-random-api.ml/animal/fox')
                foxjson = await request.json()
                request2 = await session.get('https://some-random-api.ml/facts/fox')
                factjson = await request2.json()

            embed = nextcord.Embed(title="Pictures | Fox", description=factjson['fact'], color=0x49FF2c)
            embed.set_image(url=foxjson['link'])
            embed.set_footer(text=f"Information requested by {ctx.author.display_name}", icon_url=f"{ctx.author.avatar}")
            print(f"[fun.py]Someone requested a picture of a fox! What did the fox say?")
            await ctx.send(embed=embed)

        #Koala
        @commands.command()
        async def cat(self, ctx):
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://some-random-api.ml/animal/koala')
                koalajson = await request.json()
                request2 = await session.get('https://some-random-api.ml/facts/koala')
                factjson = await request2.json()

            embed = nextcord.Embed(title="Pictures | Koala", description=factjson['fact'], color=0x49FF2c)
            embed.set_image(url=koalajson['link'])
            embed.set_footer(text=f"Information requested by {ctx.author.display_name}", icon_url=f"{ctx.author.avatar}")
            print(f"[fun.py]Someone requested a picture of a koala! *Koala noises*")
            await ctx.send(embed=embed)

        #Panda
        @commands.command()
        async def cat(self, ctx):
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://some-random-api.ml/animal/panda')
                pandajson = await request.json()
                request2 = await session.get('https://some-random-api.ml/facts/panda')
                factjson = await request2.json()

            embed = nextcord.Embed(title="Pictures | Panda", description=factjson['fact'], color=0x49FF2c)
            embed.set_image(url=pandajson['link'])
            embed.set_footer(text=f"Information requested by {ctx.author.display_name}", icon_url=f"{ctx.author.avatar}")
            print(f"[fun.py]Someone requested a picture of a panda! They are so cuteeeee!!!")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(fun(client))
