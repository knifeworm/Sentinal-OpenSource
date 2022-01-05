#Imports
import nextcord
from nextcord.ext import commands

#Setup
class Moderation(commands.cog):

    def __init__(self, client):
        self.client = client

#Events
#Commands
    #Test
    @commands.command()
    async def moderationtest(self):
        print('[moderatiom.py] Tests Comming Soon!' )


#End
def setup(client):
    client.add_cog(Moderation(client))
