#Imports
import discord
from discord.ext import commands

#Setup
class Moderation(commands.cog):

    def __init__(self, client):
        self.client = client

#Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('[moderation.py] 100% Loaded!')

#Commands
    #Test
    @commands.command()
    async def moderationtest(self):
        print('[moderatiom.py] Tests Comming Soon!' )


#End
def setup(client):
    client.add_cog(Moderation(client)):
