#Bot Made By: FuneralIowa919
import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import random
from discord.ext.commands import Bot
import sys
from discord import Game



TOKEN = 'NDg0ODk3NTI1OTQ2Mzg0Mzg0.DoXyCg.1_J3YBHhLUf4AYxXhXQRx-NF9WY'
bot = commands.Bot(command_prefix= '-live ')
bot.remove_command('help')
Bot = discord.Client()
Client = discord.Client()




@bot.event
async def on_ready():
    print("Bot Connected To Discord!")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    channel = ctx.message.channel

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Info For User: {}'.format(user.name))
    embed.add_field(name='Users ID:', value=user.id, inline=True)
    embed.add_field(name='User Status:', value=user.status, inline=True)
    embed.add_field(name='Users Top Role:', value=user.top_role, inline=True)
    embed.add_field(name='User Joined:', value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.listen()
async def on_member_join(member):
    await bot.send_message(member, "Please Accept The Rules By Going To: #server-rules and hitting: :white_check_mark:")

@bot.command()
async def ping():
    await bot.say('Pong! :ping_pong: ')

@bot.command(hidden=True)
@commands.has_role("Owners")
async def kill():
    await bot.say("Bye Bye!")
    await bot.logout()

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Help')
    embed.add_field(name='CMD Prefix', value='**-live**', inline=False)
    embed.add_field(name='Help', value='Shows This Message', inline=False)
    embed.add_field(name='Ping', value='Returns: Pong :ping_pong:', inline=False)
    embed.add_field(name='Test', value='Sends A Test Message', inline=False)
    embed.add_field(name='Echo', value='Bot Repeats Whatever Is Said After: __**Echo**__', inline=False)
    embed.add_field(name='Info', value='Gives the info for the username requested', inline=False)
    embed.add_field(name='Kick', value='Kicks the user named **__ADMIN/OWNER ONLY__**', inline=False)
    embed.add_field(name='Ban', value='Bans the user named **__ADMIN/OWNER ONLY__**', inline=False)
    embed.add_field(name='Join My Develpers Server!', value="https://discord.gg/TFE443N", inline=False)

    await bot.say("**Check Your DMs {}**".format(ctx.message.author))
    await bot.send_message(author, embed=embed)


    
@bot.command()
async def test():
    await bot.say('TEST MSG!')


@bot.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await bot.say(output)


@bot.command(pass_context = True, hidden=True)
async def clear(ctx, number=1):
    mgs = [] 
    number = int(number) + 1
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)

@bot.command(pass_context=True)
@commands.has_role("Owners")
async def kick(ctx, user: discord.Member):
    await bot.say(":middle_finger: Get The Fuck Out {}".format(user.name))
    await bot.send_message
    await bot.kick(user)

@bot.command(pass_context=True)
@commands.has_role("Owners")
async def ban(ctx, user: discord.Member):
    await bot.say(":middle_finger: Stay The Fuck Out {}".format(user.name))
    await bot.ban(user)

bot.run(TOKEN)