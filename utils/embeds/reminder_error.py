import discord 

def reminder_error():
    embed = discord.Embed(
        title="Reminder Error",
        description="A reminder was not set from your account",
        color=discord.Color.red()
    )
    embed.add_field(
        name="Help",
        value="type -> !deno remind"
    )
    return embed