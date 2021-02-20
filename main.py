import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = "!", description = "Mon bot")

#event ready
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('𝐵𝐿𝑀 𝐶𝑜𝑚𝑚𝑢𝑛𝑖𝑡𝑦 On TOP'))
    print("Bot is Ready ! ")

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


#command kick
@bot.command()
async def kick(ctx, user :discord.User, *reason):
    print(reason)
    reason = "".join(reason)
    await ctx.guild.kick(user,reason = reason)
    await ctx.send(f"{user} à été kick du Discord. {reason} ")

#command ban
@bot.command()
async def ban(ctx, user :discord.User, *reason):
    print(reason)

bot.run("TOKEN+")

