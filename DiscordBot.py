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
        if choice.split("(", 1)[0] in dir(clientCommands):
            if "(" in choice:
                func = getattr(clientCommands, choice.split("(",1)[0])
                execPrefix = ""
                if inspect.iscoroutinefunction(func):
                    execPrefix = "await "
                print("Running Command: " + choice)
                loop = False
                print(("async def mainCode(self):\n\t" + execPrefix + "self." + choice.replace("self", "").replace("self, ", "")))
                exec("async def mainCode(self):\n\t" + execPrefix + "self." + choice.replace("self", "").replace("self, ", ""), globals())
                await mainCode(self)
#---Client Commands---
class clientCommands():
    def __init__(self, client):
        self.client = client
    async def sendMessage(self, channelID):
        channel = self.client.get_channel(int(channelID))
        await channel.send("hello")
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
    print("\n------\n")
    print("Logged Into: " + str(client.user.name))
    print("Login Time: " + str(round(t1-t0, 1)) + "s")
    print("\n------\n")
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
