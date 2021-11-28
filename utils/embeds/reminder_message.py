import discord 

def send_reminder_message(time_bound,user,message):
    embed = discord.Embed(
        title="Reminder",
        color=discord.Color.dark_teal()
    )
    embed.add_field(
        name=f'Author',
        value=f'@{user.display_name}'
    )
    embed.add_field(
        name="Wait Time",
        value=f"{time_bound} seconds",
        inline=False
    )
    embed.add_field(
        name="Message",
        value=message,
        inline=False
    )
    return embed