import discord
import os
import re


intents = discord.Intents.all()
client = discord.Client(intents=intents)

ch_id = int(os.getenv('Channel_id'))
channel = client.get_channel(ch_id)

@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    #どこかのチャンネルでコメント投稿された場合に特定のチャンネルに通知する
    if re.match(r".*", message.content):
        embed=discord.Embed(title="Nofication",description='<#' + str(message.channel.id) + '>で<@' + str(message.author.id) + '>さんが発言しました。',color=0x000000)
        await client.get_channel(ch_id).send(embed=embed)
       
# Botの起動とDiscordサーバーへの接続
client.run(os.getenv('TOKEN'))
