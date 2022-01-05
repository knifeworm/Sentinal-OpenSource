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

    #Clear
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 5):
        embed = nextcord.Embed(title="Moderation | Clear",description=f"{amount} messages were cleared!",color=0x61FBFB)
        embed.set_footer(text=f"Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url} {round(client.latency * 1000)}ms")
        await ctx.channel.purge(limit=amount)



#End
def setup(client):
    client.add_cog(Moderation(client))
