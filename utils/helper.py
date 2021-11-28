import discord 
from utils.embeds.helper import create_helper_embed

async def helper_command(channel):
    await channel.send(embed=create_helper_embed())