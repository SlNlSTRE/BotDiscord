import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = "!", description = "Mon bot")

class BotData:
    def __init__(self):
        self.welcome_channel = None
        self.goodbye_channel = None

botdata = BotData()


#event ready
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('𝐵𝐿𝑀 𝐶𝑜𝑚𝑚𝑢𝑛𝑖𝑡𝑦 On TOP'))
    print("Bot is Ready ! ")

@bot.event
async def on_member_join(member):
    if botdata.welcome_channel != None:
        await botdata.welcome_channel.send(f"Bienvenue! {member.mention}")

    else:
        print("Welcome channel was not set.")

@bot.event
async def on_member_remove(member):
    if botdata.welcome_channel != None:
        await botdata.goodbye_channel.send(f"Aurevoir! {member.mention}")

    else:
        print("Goodbye channel was not set.")


@bot.command()
async def set_welcome_channel(ctx, channel_name=None):
    if channel_name != None:
        for channel in ctx.guild.channels:
            if channel.name == channel_name:
                botdata.welcome_channel = channel
                await ctx.channel.send(f"Le channel Bienvenue a été réglée sur: {channel.name}")
                await channel.send("c'est le nouveau channel d'accueil")

    else:
        await ctx.channel.send("Vous n'avez pas inclus le nom du channel de bienvenue.")


@bot.command()
async def set_goodbye_channel(ctx, channel_name=None):
    if channel_name != None:
        for channel in ctx.guild.channels:
            if channel.name == channel_name:
                botdata.goodbye_channel = channel
                await ctx.channel.send(f"Le channel aurevoir a été réglée sur: {channel.name}")
                await channel.send("c'est le nouveau channel d'aurevoir ")

    else:
        await ctx.channel.send("Vous n'avez pas inclus le nom du channel de d'aurevoir.")





#commande say
@bot.command()
async def say(ctx, *texte):
	await ctx.send(" ".join(texte))


#ping du bot
@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}ms!')


#command clear
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)




#Command dm
@bot.command()
@commands.has_permissions(manage_messages=True)
async def dm(ctx, user_id=None, *, args=None):
    if user_id != None and args != None:
        try:
            target = await bot.fetch_user(user_id)
            await target.send(args)

            await ctx.channel.send("'" + args + "'a été envoyé à: " + target.name)

        except:
            await ctx.channel.send("Impossible de dm l'utilisateur donné.")

bot.run("TOKEN+")

