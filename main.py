import discord

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    """Event listener for when the bot has switched from offline to online"""
    print(f'{bot.user} is now connected')

@bot.event
async def on_message(message):
    """Event listener for when a message is sent"""
