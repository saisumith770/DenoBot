import discord

from utils.greeting import welcome_message
from config import *
from utils.invites import (
    get_invites, 
    get_invite_info,
    add_channel_invite,
    remove_invite
)
from utils.helper import helper_command

class DenoBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.guilds = True

        super().__init__(intents=intents)
        self.__version__ = discord.__version__
        self.name = BOT_NAME

        print("bot is up and running")

    async def on_member_join(self,member):
        channel = self.get_channel(WELCOME_CHANNEL)
        await channel.send(welcome_message(member.display_name))

    async def on_message(self,message):
        content = message.content
        if content.startswith("!deno"):
            channel = message.channel
            content = content.lstrip("!deno ").split(' ')
            #----------------Helper Functions------------------
            if(content[0] == "commands" or content[0] == "help"): await helper_command(channel)
            #----------------Invite Functions------------------
            elif(content[0] == "invites"): await get_invites(self,channel)
            elif(content[0] == "invite_info"): await get_invite_info(self,channel,content[1])
            elif(content[0] == "add_invite"): 
                if(len(content) > 1): 
                    if(len(content) > 2):
                        params = content[2].split(',')
                        await add_channel_invite(
                            self,
                            content[1],
                            channel,
                            int(params[0]),
                            int(params[1]),
                            params[2] == "True"
                        )
                    elif("," in content[1]): await add_channel_invite(
                        self,
                        "#select-random-channel",
                        channel,
                        int(params[0]),
                        int(params[1]),
                        params[2] == "True"
                    )
                    else: await add_channel_invite(self,content[1],channel)
                else: await add_channel_invite(self,"#select-random-channel",channel)
            elif(content[0] == "remove_invite"):
                if len(content) > 1: await remove_invite(self,channel,content[1])
                else: await remove_invite(self,channel)
            #----------------Reminder Functions------------------
            elif(content[0] == "remind"): pass 
            #----------------Music Functions------------------
            elif(content[0] == "play"): pass

    # async def on_member_remove(self,member):
    #     await member.send("oops")
    #     print(f"{member.display_name} left")

bot = DenoBot()
bot.run(BOT_TOKEN)