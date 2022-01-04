# JUST TO TEST IF LOADING SYSTEM WORKS
import nextcord
from nextcord.ext import commands

class test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Test")

def setup(client):
    client.add_cog(test(client))