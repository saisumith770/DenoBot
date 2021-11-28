import discord

def invalid_command_embed():
    embed = discord.Embed(
        title="Invalid Command",
        description="The above command is not recognized by the servers. Report this error to @AR#8244",
        color=discord.Color.red()
    )
    return embed