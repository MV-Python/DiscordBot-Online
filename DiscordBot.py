#rewrite
print('''
   _____________                  ___________
  /   __________\               /_________   \\
 |   /███████████████████████████████████ |  |
 |  | █▄─▄▄▀█▄─▄█─▄▄▄▄█─▄▄▄─█▄─▄▄─█▄─█─▄█ |  |
(o  o)██─██─██─██▄▄▄▄─█─███▀██─▄▄▄██▄─▄██ |  |
 \__/ ▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▀▀▄▄▄▀▀/  /
  |               \__________/ _________/  /
  ^     Viper 2.0  \ \ \ \ \ \ \__________/
''')

#---Imports---
import asyncio
import discord
import time
#---Client Commands---
client = discord.Client()
def restart():
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
class clientCommands():
    def __init__(self, client):
        self.client = client

TOKEN = input("Token   > ")
TOKEN = TOKEN.strip('''"''')
BOT = input("Bot T/F > ")
if BOT in ["false", "False", "f", "F"]:
    BOT = False
else:
    BOT = True
bot = clientCommands(client = client)

@client.event
async def on_ready():
    t1 = time.time()
    print("ready")
    print(str(round(t1-t0, 1)) + "s Login Time")

print("loading...")
t0 = time.time()
client.run(TOKEN, bot=BOT)
