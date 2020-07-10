#rewrite
print('''
   _____________                 ___________
  /   ________   \              /   _____   \\
 |  / ███████████████████████████████████|  |
 |  | █▄─▄▄▀█▄─▄█─▄▄▄▄█─▄▄▄─█▄─▄▄─█▄─█─▄█|  |
(o  o)██─██─██─██▄▄▄▄─█─███▀██─▄▄▄██▄─▄██|  |
 \__/ ▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▀▀▄▄▄▀▀/  /
  |              \____________/_________/  /
  ^     Viper 2.0  \ \ \ \ \ \ \__________/
''')

#---Imports---
import asyncio
import discord
import time
import inspect
import subprocess
#---Local Functions---
async def controlPanel(self):
    global loop
    while loop == True:
        choice = input(" >>> ")
        if choice == "help":
            print("Command List\n------------")
            for command in dir(clientCommands):
                if not command.startswith("__"):
                    if command != "help":
                        print(command + str(inspect.signature(getattr(clientCommands, command))).replace("self, ", "").replace("self", ""))
        if choice == "run":
            loop = False
        if choice.split("(", 1)[0] in dir(clientCommands):
            if "(" in choice:
                func = getattr(clientCommands, choice.split("(",1)[0])
                execPrefix = ""
                if inspect.iscoroutinefunction(func):
                    execPrefix = "await "
                print("Running Command: " + choice + "...\n")
                exec("async def mainCode(self):\n\ttry:\n\t\t" + execPrefix + "self." + choice.replace("self, ", "").replace("self", "") + "\n\texcept Exception as e:\n\t\tprint('Error: ' + str(e))", globals())
                await mainCode(self)
#---Client Commands---
class clientCommands():
    def __init__(self, client):
        self.client = client
    async def sendMessage(self, channelID, message):
        channel = self.client.get_channel(int(channelID))
        await channel.send(message)
        print("Message sent")
    def autoListen(self):
        global loop
        @self.client.event
        async def on_message(message):
            print(message.author.name + " > " + message.content)
        loop = False
client = discord.Client()
bot = clientCommands(client = client)
#---Running---
@bot.client.event
async def on_ready():
    global loop
    t1 = time.time()
    print("\n------")
    print("Logged Into: " + str(client.user.name))
    print("Login Time: " + str(round(t1-t0, 1)) + "s")
    print("------\n")
    loop = True
    while loop == True:
        await controlPanel(bot)
    @bot.client.event
    async def on_ready():
        pass
#----Live Loop---
TOKEN = input("Token   > ")
TOKEN = TOKEN.strip('''"''')
BOT = input("Bot T/F > ")
if BOT in ["false", "False", "f", "F"]:
    BOT = False
else:
    BOT = True

print("loading...")
t0 = time.time()
client.run(TOKEN, bot=BOT)
