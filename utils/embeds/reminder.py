import discord

def start_reminder_embed():
    embed = discord.Embed(
        title="Reminder",
        description="setting a reminder for a given number of seconds",
        color=discord.Color.teal()
    )
    embed.add_field(
        name="!deno remind",
        value="starts the reminder process",
        inline=False
    )
    embed.add_field(
        name="!deno message <message>",
        value="message that would be presented",
        inline=False
    )
    embed.add_field(
        name="!deno time <time in seconds>",
        value="waiting time in seconds",
        inline=False
    )
    return embed