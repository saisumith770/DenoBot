from os import environ
import discord

from utils.embeds.invite_info import create_invite_info_embed

async def get_invites(server,channel):
    for guild in server.guilds:
        if guild.name == environ.get("SERVER"):
            invites = await guild.invites()
            for invite in invites:
                await channel.send(invite.url)
            break

async def get_invite_info(server,channel,code): 
    for guild in server.guilds:
        if guild.name == environ.get("SERVER"):
            invites = await guild.invites()
            for invite in invites:
                if invite.code == code or invite.url == code:
                    await channel.send(embed=create_invite_info_embed(invite))
                    break