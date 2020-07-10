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
#---Local Functions---
async def controlPanel(self):
    loop = True
    while loop == True:
        choice = input(" >>> ")
        if choice == "help":
            print("Command List\n------------")
            for command in dir(clientCommands):
                if not command.startswith("__"):
                    if command != "help":
                        print(command + str(inspect.signature(getattr(clientCommands, command))).replace("self, ", "").replace("self", ""))
        if choice.split("(", 1)[0] in dir(clientCommands):
            if "(" in choice:
                func = getattr(clientCommands, choice.split("(",1)[0])
                execPrefix = ""
                if inspect.iscoroutinefunction(func):
                    execPrefix = "await "
                print("Running Command: " + choice + "...\n")
                exec("async def mainCode(self):\n\t" + execPrefix + "self." + choice.replace("self, ", "").replace("self", ""), globals())
                await mainCode(self)
                loop = False
#---Client Commands---
class clientCommands():
    def __init__(self, client):
        self.client = client
    async def sendMessage(self, channelID, message):
        channel = self.client.get_channel(int(channelID))
        await channel.send(message)
        print("Message sent")
    def autoListen(self):
        @self.client.event
        async def on_message(message):
            print(message.author.name + " > " + message.content)
client = discord.Client()
bot = clientCommands(client = client)
#---Running---
@bot.client.event
async def on_ready():
    t1 = time.time()
    print("\n------")
    print("Logged Into: " + str(client.user.name))
    print("Login Time: " + str(round(t1-t0, 1)) + "s")
    print("------\n")
    while True:
        await controlPanel(bot)
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
