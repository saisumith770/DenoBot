import discord
import random

def welcome_message(member):
    greeting = random.choice([
        f"Welcome @{member.display_name}👋",
        f"@{member.display_name} has joined!🎉",
        f"@{member.display_name} just landed🚀",
        f"@{member.display_name} hopped on board"
    ])
    embed = discord.Embed(
        title=greeting,
        color=discord.Color.random(),
    )
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(
        name="User",
        value=member.display_name,
        inline=True
    )
    embed.add_field(
        name="Status",
        value=member.status,
        inline=True
    )
    roles = ""
    for role in member.roles:
        roles += role.name + " "
    embed.add_field(
        name="Roles",
        value=roles,
        inline=False
    )
    return embed