from os import environ
import discord

async def add_channel_invite(
    server,
    invite_channel, 
    channel,
    max_age=300,
    max_uses=10,
    temporary=True
):
    for guild in server.guilds:
        if guild.name == environ.get("SERVER"):
            if(invite_channel == "#select-random-channel"):
                for _channel in guild.channels:
                    if(isinstance(_channel,discord.TextChannel)):
                        invite = await _channel.create_invite(
                            max_age=max_age,
                            max_uses=max_uses,
                            temporary=temporary
                        )
                        await channel.send(invite.url)
                        break
            for _channel in guild.channels:
                if(invite_channel == _channel.name):
                    invite = await _channel.create_invite(
                        max_age=max_age,
                        max_uses=max_uses,
                        temporary=temporary
                    )
                    await channel.send(invite.url)
                    break