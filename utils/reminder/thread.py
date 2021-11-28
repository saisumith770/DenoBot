from threading import Thread
from time import sleep
import asyncio

def reminder_thread(time_bound,channel,message):
    async def async_executable():
        await asyncio.sleep(time_bound)
        await channel.send(message)
    
    task = asyncio.create_task(async_executable())