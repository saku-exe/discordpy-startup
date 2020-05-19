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

async def on_message(message):
    if message.content == '/cleanup':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('はいはいわかりましたよ～')
        else:
            await message.channel.send('何様のつもり？')
        
        
ID_CHANNEL_WELCOME =  688709651168100366 # 入室用チャンネルのID(int)
ID_ROLE_WELCOME =　712224759386996766  #付けたい役職のID(int)
EMOJI_WELCOME = '🍼' # 対応する絵文字




# リアクション追加時に実行されるイベントハンドラを定義
@client.event
async def on_raw_reaction_add(payload):
    # 役職を付与する非同期関数を実行して Optional[Member] オブジェクトを取得
    member = await grant_role(payload)
    if member is not None: # 役職を付与したメンバーがいる時
        text = f'{member.mention} つけたよ～'
        await message.channel.send(text)
            
