from config import *

async def generate_invites(server,channel):
    for guild in server.guilds:
        if guild.name == SERVER:
            invites = await guild.invites()
            for invite in invites:
                await channel.send(invite.url)
            break