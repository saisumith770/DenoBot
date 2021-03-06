from os import environ
from dotenv import load_dotenv
import discord

from utils.embeds.greeting import welcome_message
from utils.invites import (
    get_invites, 
    get_invite_info,
    add_channel_invite,
    remove_invite
)

from utils.embeds.reminder import start_reminder_embed
from utils.reminder.thread import reminder_thread
from utils.embeds.reminder_error import reminder_error
from utils.embeds.invalid_command import invalid_command_embed
from utils.embeds.helper import create_helper_embed

load_dotenv()

class DenoBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.guilds = True

        super().__init__(intents=intents)
        self.__version__ = discord.__version__
        self.name = environ.get("BOT_NAME")
        self.reminder_setters = []
        self.reminder_queue = []

        print("bot is up and running")

    async def on_member_join(self,member):
        channel = self.get_channel(environ.get("WELCOME_CHANNEL"))
        await channel.send(embed=welcome_message(member))

    async def on_message(self,message):
        content = message.content
        if content.startswith("!deno"):
            channel = message.channel
            content = content.lstrip("!deno ").split(' ')
            #----------------Helper Functions------------------
            if(content[0] == "commands" or content[0] == "help"): await channel.send(embed=create_helper_embed())
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
            elif(content[0] == "remind"): 
                self.reminder_setters.append(message.author)
                await channel.send(embed=start_reminder_embed())
            elif content[0] == "message":
                if(message.author in self.reminder_setters):
                    _message = ""
                    content.remove("message")
                    for word in content:
                        _message += word + ' '
                    self.reminder_queue.append({
                        "user":message.author,
                        "message": _message
                    }) 
                    self.reminder_setters.remove(message.author)
                else: await channel.send(embed=reminder_error())
            elif content[0] == "time":
                for member in self.reminder_queue:
                    if(member["user"] == message.author): 
                        reminder_message = member["message"]
                        self.reminder_queue.remove(member)
                        reminder_thread(int(content[1]),channel,message.author,reminder_message)
                        break
                else: await channel.send(embed=reminder_error())
            #----------------Music Functions------------------
            elif(content[0] == "play"): pass
            #----------------Invalid Command------------------
            else: await channel.send(embed=invalid_command_embed())

    # async def on_member_remove(self,member):
    #     await member.send("oops")
    #     print(f"{member.display_name} left")

if __name__ == "__main__":
    bot = DenoBot()
    bot.run(environ.get("BOT_TOKEN"))