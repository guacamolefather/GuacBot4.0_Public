import discord
from discord.ext import commands, bridge
from cogs.extraclasses.read import *
from translate import Translator
from cogs.extraclasses.perms import *

class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Utility processes active.")

    @bridge.bridge_command(description="Tests if the Utility cog is loaded.")
    @commands.check(is_it_me)
    async def utilitytest(self, ctx):
        await ctx.respond('Utility extension cog works!')

    @bridge.bridge_command(description="Pings Guac.")
    @commands.check(is_it_me)
    async def ping(self, ctx):
        await ctx.respond('Latency: ' + str(round(self.bot.latency * 1000)) + 'ms.')

    @bridge.bridge_command(description="Shows the avatar of the given member (or user if not given).")
    async def avatar(self, ctx, member : discord.Member=None):
        if (member == None):
            member = ctx.author
        memberAvatarUrl = member.avatar.url
        await ctx.respond(memberAvatarUrl)
    
    @bridge.bridge_command(description="Returns an image of the given emoji.")
    async def emojiimage(self, ctx, *, msg):
        if not msg.startswith("<"):
            await ctx.respond("Just an emoji, pls.")
            return
        
        try:
            _id = msg.split(":") # split by ":"
            if "<a" == _id[0]: # animated emojis structure <a:name:id>
                ext = "gif"
            else:
                ext = "png" # normal emojis structure <name:id>
            e_id = _id[2].split(">")[0].strip()# get the id
            # url for a emoji is like this
            url = f"https://cdn.discordapp.com/emojis/{e_id}.{ext}"

            await ctx.respond(f"**Name**: :{_id[1]}: **Link**: {url}")
            
        except:
            await ctx.respond("Just an emoji, pls.")
    
    @bridge.bridge_command(aliases=["count","attendence"], description="Shows details about all server members.")
    async def rolecall(self, ctx):
        notbots = 0
        #withrole = 0
        online = 0
        icon_url = ctx.guild.icon.url
        embed = discord.Embed(title="Rolecall", description=f"{ctx.guild.member_count} members including me :)")
        embed.set_thumbnail(url=icon_url)

        #not bot members
        for member in ctx.guild.members:
            if not member.bot:
                notbots += 1
        embed.add_field(name='"Human" Member(s):',value=notbots, inline=False)

        #members in roles
        #for role in ctx.guild.roles:
            #for member in ctx.guild.members:
                #if role in member.roles:
                    #withrole += 1
            #embed.add_field(name=f"{role} members:",value=withrole, inline=False)
            #withrole = 0
        
        #online members
        for member in ctx.guild.members:
            if (str(member.status) == "online" or str(member.status) == "dnd") and not member.bot:
                online += 1
        embed.add_field(name='"Human" Member(s) Online/DND:',value=online, inline=False)

        await ctx.respond(embed=embed)
        
    @bridge.bridge_command(description="Returns server data on the user.")
    async def profile(self, ctx): #, *, member : discord.Member=None):
        #if (member == None):
        member = ctx.author
        embed = discord.Embed(title=str(member), description="Member's statistics:", colour=member.top_role.color, url="https://www.youtube.com/watch?v=iik25wqIuFo")
        embed.set_thumbnail(url=member.avatar.url)

        #Member's roles:
        member_roles = []
        fancy_roles_list = ""
        if (len(member.roles) > 1):
            raw_list = [role.mention for role in member.roles]
            raw_list.pop(0)
            for i in raw_list:
                member_roles.insert(0, i)
            for role in member_roles:
                fancy_roles_list = fancy_roles_list + "- " + role + "\n"
        else:
            fancy_roles_list = "None"
        embed.add_field(name="Role(s):",value=fancy_roles_list, inline=False)
        
        #How many channels member has access to:
        counter = 0
        for channel in ctx.guild.text_channels:
            if (channel.permissions_for(member).read_messages):
                counter = counter + 1
        embed.add_field(name="Channels:",value="Has access to " + str(counter) + " channels.",inline=False)

        embed.add_field(name="Messages sent:", value="at least 2?", inline=False)

        embed.add_field(name="Regular profile",value="This is the regular profile command. For the admin command, use $adminprofile (with admin priviledges).", inline=False)

        await ctx.respond(embed=embed)

    @bridge.bridge_command(description="Returns the list of Guac's reactions.")
    async def reactions(self, ctx):
        triggers = ReadTriggers()
        fancyList = ""
        for i in triggers:
            if not isinstance(i, str):
                if fancyList.endswith(", "):
                    fancyList = fancyList + "("
                else:
                    fancyList = fancyList + ", ("
                for subtrigger in i:
                    if fancyList.endswith("("):
                        fancyList = fancyList + subtrigger
                    else:
                        fancyList = fancyList + ", " + subtrigger
                fancyList = fancyList + "), "
            else:
                if i == "409445517509001216":
                    fancyList = "@thememesareallreal"
                else:
                    if fancyList.endswith(", "):
                        fancyList = fancyList + i
                    else:
                        fancyList = fancyList + ", " + i
        await ctx.respond(fancyList)
    
    @bridge.bridge_command(description="Translates to specified lang from specified lang (using 2 letter ISO codes) the specified words.")
    async def translate(self, ctx, to_lang: str, from_lang: str, *, words: str):

        translator= Translator(to_lang=to_lang, from_lang=from_lang)

        translated = translator.translate(words)

        await ctx.respond(translated)

def setup(bot):
    bot.add_cog(Utility(bot))
