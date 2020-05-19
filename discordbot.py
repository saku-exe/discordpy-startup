from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def toa(ctx):
    await ctx.send('なに～なんか用？')


bot.run(token)
##########################################################################################
async def on_message(message):
    if message.content == '/削除':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('はいはいわかりましたよ～')
        else:
            await message.channel.send('何様のつもり？')
