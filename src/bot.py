import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from services.deepseek_api import get_deepseek_response
import commands as cmds

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command(name='ask')
async def ask_deepseek(ctx, *, question: str):
    await cmds.ask_deepseek(ctx, question=question)

bot.run(TOKEN)