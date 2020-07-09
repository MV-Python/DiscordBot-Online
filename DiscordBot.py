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
#---Client Commands---
class clientCommands():
    def __init__(self, client):
        self.client = client
    def controlPanel(self):
        loop = True
        while loop == True:
            choice = input(" >>> ")
            if choice in dir(clientCommands):
                func = getattr(clientCommands, choice)
                func(self)
                print("---done---")
    #Control Commands
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
    bot.controlPanel()
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
