import discord
import os
from dotenv import load_dotenv
from openai import OpenAI

# .envファイルから環境変数を読み込む
load_dotenv()

# 環境変数からDiscord Botのトークンを設定
TOKEN = os.getenv('DISCORD_TOKEN')

# Discord Botのクライアントを作成
client = discord.Client(intents=discord.Intents.all())

# Discord Bot起動時
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # noko_data.txtからプロンプトテンプレートを読み込む
    with open('noko_data.txt', 'r') as file:
        prompt_template = file.read().strip()

    openai_clent = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    messages = [
        {"role": "system", "content": prompt_template},
        {"role": "user", "content": message.content}
    ]

    completion = openai_clent.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=150
    )
    
    response = completion.choices[0].message.content

    # 応答を送信する
    await message.channel.send(response)

# Discord Botを起動する
client.run(TOKEN)
