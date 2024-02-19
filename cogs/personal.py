import discord
from discord.ext import commands, bridge
from cogs.extraclasses.perms import *
from cogs.extraclasses.jason import *

data = FetchBotData()

class Personal(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Personal shit active.')

    @bridge.bridge_command(description="Adds something to the to-do list.")
    @commands.check(is_it_me)
    async def todo(self, ctx, *, do: str):
        with open('z_ToDoList.txt', 'a', encoding='utf-8') as writer:
            writer.write(f"\n - {do}")
        writer.close()

        channel = self.bot.get_channel(813974138581942282)
        await channel.send(f"- {do}")
        
        await ctx.respond('Added to the list!')

    @bridge.bridge_command(description="Adds a new nickname to the list.")
    @commands.check(is_it_me)
    async def nickname(self, ctx, *, name: str):
        with open('z_Nicknames.txt', 'a', encoding='utf-8') as writer:
            writer.write(f"\n- {name}")
        writer.close()
        
        await ctx.respond('Added to the list!')

def setup(bot):
    bot.add_cog(Personal(bot))