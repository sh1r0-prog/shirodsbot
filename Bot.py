import discord
import os

from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix= "s!")


mute_role = discord.utils.get(ctx.message.guild.roles, name= 'таймач😫')


@Bot.command()
async def info(ctx):
    author = ctx.message.author
    await ctx.send("Этот бот в разроботке! Вы можете предложить свои идеи и высказать недовольство тут: https://discord.gg/ykdtjYY")
    
@Bot.command()
@commands.has_permissions(administrator= True)
async def mute(ctx, member: discord.Member):
    await member.add_roles(mute_role)
    

token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))
