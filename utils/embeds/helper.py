import discord

commands = [
    {"cmd":'!deno commands',"purpose":"shows deno commands"},
    {"cmd":'!deno help',"purpose":"shows deno commands"},
    {"cmd":'!deno invites',"purpose":"shows server invites"},
    {"cmd":'!deno invite_info <invite code | invite url>',"purpose":"shows invite info"},
    {"cmd":'!deno add_invite <channel name>(optional) <age,uses,temporary>(optional)',"purpose":"adds new invite"},
    {"cmd":'!deno remove_invite <invite code | invite url>(optional)',"purpose":"removes old invite"},
    {"cmd":'!deno remind',"purpose":"starts a reminder process"},
    {"cmd":'!deno message <message>',"purpose":"sets the reminder message"},
    {"cmd":"!deno time <time in seconds>","purpose":"sets the time for the message"}
]

def create_helper_embed():
    embed = discord.Embed(
        title= "DenoBot Commands",
        description="'<>' signifies you would enter respective details and '|' signifies or",
        color= discord.Color.magenta()
    )
    for cmd in commands:
        embed.add_field(
            name=cmd["cmd"],
            value=cmd["purpose"],
            inline=False
        )
    return embed