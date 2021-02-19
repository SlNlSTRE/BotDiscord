import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = "!", description = "Mon bot")

#event ready
@bot.event
async def on_ready():
    print("Ready ! ")

#commande say
@bot.command()
async def say(ctx, *texte):
	await ctx.send(" ".join(texte))



#command clear
@bot.command()
async def clear(ctx, nombre : int):
    messages = await ctx.channel.history(limit = nombre + 1).flatten()
    for message in messages:
        print(message)
        await message.delete()
				
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

bot.run("ODA4NzcxMDAwNTM5OTM4ODI2.YCLYsA.prF7GJVkFlDD6iFEaiyfykt2qds")
