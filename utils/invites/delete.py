from config import *

async def remove_invite(server,channel,invite_code = "-a"):
    for guild in server.guilds:
        if guild.name == SERVER:
            invites = await guild.invites()
            if(invite_code == "-a"):
                for invite in invites:
                    await invite.delete()
                    await channel.send(f"{invite.url} was deleted")
                break
            else:
                for invite in invites:
                    if(invite.code == invite_code or invite.url == invite_code):
                        await invite.delete()
                        await channel.send(f"{invite.url} was deleted")
                        break