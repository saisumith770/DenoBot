from threading import Thread
from time import sleep
import asyncio

from utils.embeds.reminder_message import send_reminder_message

def reminder_thread(time_bound,channel,user,message):
    async def async_executable():
        await asyncio.sleep(time_bound)
        await channel.send(user.mention)
        await channel.send(embed=send_reminder_message(time_bound,user,message))
    
    task = asyncio.create_task(async_executable())