import discord
from discord.ext import commands, bridge
import random
from cogs.extraclasses.perms import *

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun processes active.")

    @bridge.bridge_command(description="Tests if the Fun cog is loaded.")
    @commands.check(is_it_me)
    async def funtest(self, ctx):
        await ctx.respond('Fun extension cog works!')

    @bridge.bridge_command(aliases=['8ball'], description="Guac answers your question.")
    async def eightball(self, ctx, *, question: str):
        responses = ['Hmmmm.','Ask again.',"It's possible.",'Maybe.','Perhaps.','Not sure.','Uncertain.','(͡° ͜ʖ ͡°)','No clue.','Response hazy.']
        await ctx.respond(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @bridge.bridge_command(aliases=['rd', 'diceroll'], description="Rolls specified sided die a specified amount of times.")
    async def rolldice(self, ctx, sides=6, amount=1):
        diceList=[]
        for i in range(0, amount):
            diceList.append(random.randint(1,sides))
            i = i + 1
        await ctx.respond("Your roll(s) are:  " + str(diceList))

    @bridge.bridge_command(description="Play a game of Rock, Paper, Scissors against Guac!")
    async def rps(self, ctx, choice: str):
        botchoice = random.randint(0, 2)
        if botchoice == 0 and choice.lower() == "rock":
            await ctx.respond("I chose rock!  It's a tie!")
        elif botchoice == 0 and choice.lower() == "paper":
            await ctx.respond("I chose rock! You win!")
        elif botchoice == 0 and choice.lower() == "scissors":
            await ctx.respond("I chose rock! I win!")
        elif botchoice == 1 and choice.lower() == "rock":
            await ctx.respond("I chose paper!  I win!")
        elif botchoice == 1 and choice.lower() == "paper":
            await ctx.respond("I chose paper! It's a tie!")
        elif botchoice == 1 and choice.lower() == "scissors":
            await ctx.respond("I chose paper! You win!")
        elif botchoice == 2 and choice.lower() == "rock":
            await ctx.respond("I chose scissors!  You win!")
        elif botchoice == 2 and choice.lower() == "paper":
            await ctx.respond("I chose scissors! I win!")
        elif botchoice == 2 and choice.lower() == "scissors":
            await ctx.respond("I chose scissors! It's a tie!")
        else:
            await ctx.respond("Do you know how to play this game or are you bad at spelling..?")

    @bridge.bridge_command(aliases=['bn'], description="Returns a big number.")
    async def bignumber(self, ctx):
        for i in range(0, random.randint(1, 1000)):
            i = i * random.randint(1, 1000)
        await ctx.respond(i)

    @bridge.bridge_command(aliases=['brn'], description="Returns a bigger number.")
    async def biggernumber(self, ctx):
        for i in range(1000, random.randint(1001, 1000000)):
            i = i * random.randint(1000, 1000000)
        await ctx.respond(i)

    @bridge.bridge_command(aliases=['bstn'], description="Returns a biggest number (might be too big for char count).")
    async def biggestnumber(self, ctx):
        for i in range(0, random.randint(1, 1000)):
            i = i ** random.randint(1, 1000)
        await ctx.respond(i)

    @bridge.bridge_command(aliases=["rn"], description="Returns a random number from a specified number to a specified number.")
    async def randomnumber(self, ctx, num1: int, num2: int):
        if (num2 > num1):
            num = random.randint(num2, num1)
        else:
            num = random.randint(num1, num2)
        await ctx.respond(num)

    @commands.command(hidden=True, description="You shouldn't be able to see this...")
    async def secret(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("SHH!!!", delete_after=3)
    
    #https://www.countryliving.com/life/a27452412/best-dad-jokes/
    @bridge.bridge_command(aliases=['joke'], description="Asks Guac to turn the thermostat down.")
    async def dadjoke(self, ctx):
        jokes = ["I'm afraid for the calendar. Its days are numbered.",
        "My wife said I should do lunges to stay in shape. That would be a big step forward.",
        "Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.",
        "I thought the dryer was shrinking my clothes. Turns out it was the refrigerator all along.",
        "Dear Math, grow up and solve your own problems.",
        "Have you heard about the chocolate record player? It sounds pretty sweet.",
        "I only know 25 letters of the alphabet. I don't know y.",
        "A skeleton walks into a bar and says, 'Hey, bartender. I'll have one beer and a mop.'",
        "I asked my dog what's two minus two. He said nothing.",
        "I don't trust those trees. They seem kind of shady.",
        "My wife is really mad at the fact that I have no sense of direction. So I packed up my stuff and right!",
        "I don't trust stairs. They're always up to something."]
        i = len(jokes) - 1
        jokechoice = random.randint(0, i)
        await ctx.respond(jokes[jokechoice])

    #https://minecraft.fandom.com/wiki/Death_messages
    @bridge.bridge_command(description="Kills the specified member.")
    @commands.check(sophie)
    async def kill(self, ctx, member : discord.Member):
        if member.id == ctx.author.id:
            await ctx.respond("Do you need a lighthouse??")
            return
        if member.id == 409445517509001216 and random.randint(1, 10) != 8:
            await ctx.respond("Dad can't be killed??")
            return
        if member.id == 582337819532460063:
            await ctx.respond("Please don't kill me...")
            return
        dead = member.display_name
        killer = ctx.author.display_name
        deaths = [f"{dead} was shot.",
        f"{dead} blew themselves up!",
        f"{dead} fell to their death...",
        f"{dead} was pummeled by {killer}.",
        f"{dead} was pricked to death via cactus!",
        f"{dead} drowned...",
        f"{dead} experienced kinetic energy...",
        f"{dead} went up in flames!",
        f"{dead} was impaled!",
        f"{dead} was squashed by {killer}...",
        f"{dead} went out with a bang!",
        f"{dead} tried to swim in lava...",
        f"{dead} discovered the floor was lava!",
        f"{dead} was struck by lightning!",
        f"{dead} froze to death...",
        f"{dead} was slain by {killer}!",
        f"{dead} took the L.",
        f"{killer} handed {dead} the L."]
        i = len(deaths) - 1
        deathchoice = random.randint(0, i)
        await ctx.respond(deaths[deathchoice])

def setup(bot):
    bot.add_cog(Fun(bot))
