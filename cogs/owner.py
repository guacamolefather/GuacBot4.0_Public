import discord
import asyncio
from discord.ext import commands, bridge
from cogs.extraclasses.read import *
from cogs.extraclasses.jason import *
from cogs.extraclasses.perms import *

botData = FetchBotData()
serverData = FetchServerData()

class Owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Owner processes active.")

    @bridge.bridge_command(description="Tests if the Owner cog is loaded.")
    @commands.check(is_it_me)
    async def ownertest(self, ctx):
        await ctx.respond('Owner extension cog works!')
    
    @bridge.bridge_command(description="Makes Guac send a TTS message with the specified words.")
    @commands.check(is_it_me)
    async def faketts(self, ctx, *, words: commands.clean_content):
        await ctx.respond(words, tts=True)
    
    @bridge.bridge_command(description="Changes Guac's status.")
    @commands.check(is_it_me)
    async def changestatus(self, ctx, activity: str, *, status: str):
        # Setting "Listening" status
        if "listen" == activity.lower():
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status))

        # Setting "Watching" status
        elif "watch" == activity.lower():
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))

        # Setting "Streaming" status
        elif "stream" == activity.lower():
            await self.bot.change_presence(activity=discord.Streaming(name=status, url="https://www.twitch.tv/thememesareallreal"))

        # Setting broken custom status
        elif "custom" == activity.lower():
            await self.bot.change_presence(activity=discord.CustomActivity(name=status))
            
        # Setting "Playing" status
        else:
            await self.bot.change_presence(activity=discord.Game(status))

        await ctx.respond("Status changed!")

    @bridge.bridge_command(description="Globally Guac blacklists the specified member.")
    @commands.check(is_it_me)
    async def globalblacklist(self, ctx, member : discord.Member):
        botData["Reactions"]["global_blacklist"].append(member.id)
        UpdateBotData(botData)
        await ctx.respond(f"{member.display_name} now on Guac global blacklist.")

    @bridge.bridge_command(description="Globally Guac unblacklists the specified member.")
    @commands.check(is_it_me)
    async def globalunblacklist(self, ctx, *, member : discord.Member):
        indexingPurposes = botData["Reactions"]["global_blacklist"]
        botData["Reactions"]["global_blacklist"].pop(indexingPurposes.index(member.id))
        UpdateBotData(botData)
        await ctx.respond(f"{member.display_name} bailed from Guac global blacklist :rolling_eyes:")

    @bridge.bridge_command(description="Shows global blacklist.")
    @commands.check(is_it_me)
    async def readblacklist(self, ctx):
        await ctx.respond(botData["Reactions"]["global_blacklist"])

    @bridge.bridge_command(description="Shows all server data.")
    @commands.check(is_it_me)
    async def allguilddata(self, ctx):
        await ctx.respond(serverData)

def setup(bot):
    bot.add_cog(Owner(bot))