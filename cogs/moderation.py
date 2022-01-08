#Imports
import nextcord
from nextcord.ext import commands
import time
import datetime
import humanfriendly

#Setup
class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

#Events

#Commands

    #Test
    @commands.command()
    async def moderationtest(self):
        await client.change_presence(status=nextcord.Status=do_not_disturb, activity=nextcord.Game("[TESTING] MODERATON.PY"))
        print('[moderatiom.py] Testing Begins In 3')
        time.sleep(1)
        print('[moderatiom.py] Testing Begins In 2')
        time.sleep(1)
        print('[moderatiom.py] Testing Begins In 1')
        time.sleep(1)
        print('[moderatiom.py] Testing Started.')
        print(f'[moderation.py]PING TEST - {round(self.client.latency * 1000)}ms')
        print('Testing done! More tests comming soon!')
        await client.change_presence(status=nextcord.Status=online, activity=nextcord.Game("ONLINE"))


    #Clear
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 5):
        embed = nextcord.Embed(title="Moderation | Clear",description=f"{amount} messages were cleared!",color=0x49FF2C)
        embed.set_footer(text=f"{round(self.client.latency * 1000)}ms Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url}")
        await ctx.send(embed=embed)
        print(f"[moderation.py]{amount} messages were cleared in {ctx.channel}")
        await ctx.channel.purge(limit=amount)

    #Kick
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : nextcord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = nextcord.Embed(title="Moderation | Kick",description=f"{member} was kicked out of the server! Reason : {reason}",color=0xFFFF43)
        embed.set_footer(text=f"{round(self.client.latency * 1000)}ms Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url}")
        print(f"[moderation.py]{member} was kicked out from the server for the reason of : {reason}")
        await ctx.send(embed=embed)
        await member.send(f"You were kicked from {ctx.guild.name}. Reason : {reason} :rage:")

    #Ban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : nextcord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = nextcord.Embed(title="Moderation | Ban",description=f"{member} was banned from the server! Reason : {reason}",color=0xFF5D3A)
        embed.set_footer(text=f"{round(self.client.latency * 1000)}ms Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url}")
        print(f"[moderation.py]{member} was banned from the server for the reason of : {reason}")
        await ctx.send(embed=embed)
        await member.send(f"You were banned from {ctx.guild.name}. Reason : {reason} :rage:")

    #Unban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        bannedUsers = await ctx.guild.bans()
        name, discrimator = member.split("#")

        for ban in bannedUsers:
            user = ban.user

            if(user.name, user.discriminator) == (name, discrimator):
                await ctx.guild.unban(user)
                embed = nextcord.Embed(title="Moderation | Unban",description=f"{member} was unbanned from the server!",color=0x49FF2C)
                embed.set_footer(text=f"{round(self.client.latency * 1000)}ms Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url}")
                print(f"[moderation.py]{member} was unbanned from the server.")
                await ctx.send(embed=embed)
                await member.send(f"You were unbanned in {ctx.guild.name}! :sunglasses:")
                return

    #Mute
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member : nextcord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = nextcord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await ctx.guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

        await member.add_roles(mutedRole, reason=reason)
        embed = nextcord.Embed(title="Moderation | Mute",description=f"{member} was muted for the reason of : {reason}",color=0xFF5D3A)
        embed.set_footer(text=f"{round(self.client.latency * 1000)}ms Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url}")
        print(f"[moderation.py]{member} was muted in the server for : {reason}")
        await ctx.send(embed=embed)
        await member.send(f"You were muted in {ctx.guild.name}. Reason : {reason} :rage:")

    #Unmute
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member : nextcord.Member):
        mutedRole = nextcord.utils = nextcord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        embed = nextcord.Embed(title="Moderation | Unmute",description=f"{member} was unmuted.",color=0x49FF2C)
        embed.set_footer(text=f"{round(self.client.latency * 1000)}ms Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url}")
        print(f"[moderation.py]{member} was unmuted in the server.")
        await ctx.send(embed=embed)
        await member.send(f"You were unmuted in {ctx.guild.name}! :sunglasses:")

    #Timeout
    @commands.command()
    async def timeout(self, ctx, member : nextcord.Member, time, *, reason):
        time = humanfriendly.parse_time(time)
        await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=time))
        embed = nextcord.Embed(title="Moderation | Timeout",description=f"{member} was timed out.",color=0x49FF2C)
        embed.set_footer(text=f"{round(self.client.latency * 1000)}ms Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url}")
        print(f"[moderation.py]{member} was timed out in the server.")
        await ctx.send(embed=embed)
        await member.send(f"You were timed out in {ctx.guild.name}! :rage:")

    #CancelTimeout
    @commands.command()
    async def canceltimeout(self, ctx, member : nextcord.Member, time, *, reason=None):
        await member.edit(timeout=None)
        embed = nextcord.Embed(title="Moderation | Canceltimeout",description=f"{member}'s timeout was cancelled.",color=0x49FF2C)
        embed.set_footer(text=f"{round(self.client.latency * 1000)}ms Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url}")
        print(f"[moderation.py]{member}'s timeout was canceled for : {reason}")
        await ctx.send(embed=embed)
        await member.send(f"Your timeout was canceled in {ctx.guild.name}! :sunglasses:")




#End
def setup(client):
    client.add_cog(Moderation(client))
