import os
import discord
from discord.ext import commands
from gtts import gTTS
from dotenv import load_dotenv
import asyncio

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
TEXT_CHANNEL_ID = int(os.getenv("TEXT_CHANNEL_ID"))
VOICE_CHANNEL_ID = int(os.getenv("VOICE_CHANNEL_ID"))
VELARIE_USER_ID = int(os.getenv("VELARIE_USER_ID"))
ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID"))
OWNER_USER_ID = int(os.getenv("OWNER_USER_ID"))
GENERAL_USER_ID = int(os.getenv("GENERAL_USER_ID"))

# Set up the bot with necessary intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Variable to store the voice connection
voice_connection = None

async def connect_to_voice_channel():
    global voice_connection
    voice_channel = bot.get_channel(VOICE_CHANNEL_ID)
    if voice_channel is not None and voice_connection is None:
        voice_connection = await voice_channel.connect()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await connect_to_voice_channel()  # Connect to voice channel on startup

@bot.event
async def on_message(message):
    global voice_connection
    if message.author == bot.user:
        return  # Ignore bot's own messages

    # Check if the message is from the specified user in the specified text channel
    if message.channel.id == TEXT_CHANNEL_ID and (message.author.id == VELARIE_USER_ID or message.author.id == ADMIN_USER_ID or message.author.id == OWNER_USER_ID or message.author.id == GENERAL_USER_ID) :
        if voice_connection is None:
            await connect_to_voice_channel()  # Reconnect if disconnected
        
        # Convert message to speech and play it in the voice channel
        await play_tts(voice_connection, message.content)

async def play_tts(vc, text):
    tts = gTTS(text=text, lang="en")
    tts.save("message.mp3")
    vc.play(discord.FFmpegPCMAudio("message.mp3"))
    
    while vc.is_playing():
        await asyncio.sleep(1)
    
    os.remove("message.mp3")  # Clean up audio file after playing

# Run the bot
bot.run(TOKEN)
