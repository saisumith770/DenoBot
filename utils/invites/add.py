from config import *

async def add_server_invite(): pass 
async def add_voice_invite(): pass 
async def add_stage_invite(): pass 
async def add_category_invite(): pass
async def add_store_invite(): pass

async def add_channel_invite(server, channel):
    for guild in server.guilds:
        if guild.name == SERVER:
            invite = await guild.create_invite()
            await channel.send(invite) 