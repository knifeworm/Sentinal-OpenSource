#Imports
import nextcord
from nextcord.ext import commands

#Setup
class Moderation(commands.Cog):

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
        embed = nextcord.Embed(title="Moderation | Clear",description=f"{amount} messages were cleared!",color=0x49FF2C)
        embed.set_footer(text=f"Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url} {round(self.client.latency * 1000)}ms")
        await ctx.send(embed=embed)
        print(f"[moderation.py]{amount} messages were cleared in {ctx.channel}")
        await ctx.channel.purge(limit=amount)

    #Kick
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = nextcord.Embed(title="Moderation | Kick",description=f"{member} was kicked out of the server! Reason : {reason}",color=0xFFFF43)
        embed.set_footer(text=f"Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url} {round(self.client.latency * 1000)}ms")
        print(f"[moderation.py]{member} was kicked out from the server for the reason of : {reason}")
        await ctx.send(embed=embed)
        await member.send(f"You were kicked from {guild.name}. Reason : {reason} :rage:")

    #Ban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = nextcord.Embed(title="Moderation | Ban",description=f"{member} was banned from the server! Reason : {reason}",color=0xFF5D3A)
        embed.set_footer(text=f"Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url} {round(self.client.latency * 1000)}ms")
        print(f"[moderation.py]{member} was banned from the server for the reason of : {reason}")
        await ctx.send(embed=embed)
        await member.send(f"You were banned from {guild.name}. Reason : {reason} :rage:")

    #Unban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        bannedUsers = await ctx.guild.bans()
        name, discrimator = member.split("#")

        for ban in bannedUsers:
            user = ban.user

            if(user.name, user,discriminator) == (name, discrimator):
                await ctx.guild.unban(user)
                embed = nextcord.Embed(title="Moderation | Unban",description=f"{member} was unbanned from the server!",color=0x49FF2C)
                embed.set_footer(text=f"Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url} {round(self.client.latency * 1000)}ms")
                print(f"[moderation.py]{member} was unbanned from the server.")
                await ctx.send(embed=embed)
                await member.send(f"You were unbanned in {guild.name}! :sunglasses:")
                return

    #Mute
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member : discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

        await member.add_roles(mutedRole, reason=reason)
        embed = nextcord.Embed(title="Moderation | Mute",description=f"{member} was muted for the reason of : {reason}",color=0xFF5D3A)
        embed.set_footer(text=f"Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url} {round(self.client.latency * 1000)}ms")
        print(f"[moderation.py]{member} was muted in the server for : {reason}")
        await ctx.send(embed=embed)
        await member.send(f"You were muted in {guild.name}. Reason : {reason} :rage:")

    #Unmute
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member : discord.Member):
        mutedRole = discord.utils = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        embed = nextcord.Embed(title="Moderation | Unmute",description=f"{member} was unmuted.",color=0x49FF2C)
        embed.set_footer(text=f"Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url} {round(self.client.latency * 1000)}ms")
        print(f"[moderation.py]{member} was unmuted in the server.")
        await ctx.send(embed=embed)
        await member.send(f"You were unmuted in {guild.name}! :sunglasses:")


#End
def setup(client):
    client.add_cog(Moderation(client))
