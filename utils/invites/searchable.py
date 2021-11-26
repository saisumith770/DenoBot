from config import *

async def get_invites(server,channel):
    for guild in server.guilds:
        if guild.name == SERVER:
            invites = await guild.invites()
            for invite in invites:
                await channel.send(invite.url)
            break

async def get_invite_info(server,channel,code): 
    for guild in server.guilds:
        if guild.name == SERVER:
            invites = await guild.invites()
            for invite in invites:
                if invite.code == code or invite.url == code:
                    await channel.send([
                        invite.url,
                        invite.channel.name, 
                        invite.code, 
                        invite.guild.name, 
                        invite.approximate_member_count,
                        invite.created_at,
                        invite.inviter,
                        invite.max_age,
                        invite.max_uses,
                        invite.uses,
                        invite.temporary,
                        invite.revoked
                    ])
                    break