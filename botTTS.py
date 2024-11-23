import os
import discord
from discord.ext import commands
from gtts import gTTS
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
TEXT_CHANNEL_ID = int(os.getenv("TEXT_CHANNEL_ID"))
VOICE_CHANNEL_ID = int(os.getenv("VOICE_CHANNEL_ID"))
VELARIE_USER_ID = int(os.getenv("VELARIE_USER_ID"))
ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID"))
# OWNER_USER_ID = int(os.getenv("OWNER_USER_ID"))
# GENERAL_USER_ID = int(os.getenv("GENERAL_USER_ID"))

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

voice_connection = None

async def connect_to_voice_channel():
    global voice_connection
    voice_channel = bot.get_channel(VOICE_CHANNEL_ID)
    if voice_channel is not None and voice_connection is None:
        voice_connection = await voice_channel.connect()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await connect_to_voice_channel()

@bot.event
async def on_message(message):
    global voice_connection
    if message.author == bot.user:
        return

    if message.channel.id == TEXT_CHANNEL_ID and (message.author.id == VELARIE_USER_ID or message.author.id == ADMIN_USER_ID):
        if voice_connection is None:
            await connect_to_voice_channel()
        
        await play_tts(voice_connection, message.content)

async def play_tts(vc, text):
    tts = gTTS(text=text, lang="en")
    tts.save("message.mp3")
    vc.play(discord.FFmpegPCMAudio("message.mp3"))
    
    while vc.is_playing():
        await asyncio.sleep(1)
    
    os.remove("message.mp3")

bot.run(TOKEN)
