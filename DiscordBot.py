#rewrite

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

    def task1(self):
        print("hi")

TOKEN = input("Token > ")
TOKEN = TOKEN.strip('''"''')
BOT = input("Bot T/F > ")
if BOT in ["true", "True", "t", "T"]:
    BOT = True
if BOT in ["false", "False", "f", "F"]:
    BOT = False
bot = clientCommands(client = client)

@bot.client.event
async def on_ready():
    bot.task1()

print("loading...")
bot.client.run(TOKEN, bot=BOT)
