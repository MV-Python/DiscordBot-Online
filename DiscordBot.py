#rewrite

#---Imports---
import asyncio
import discord
import time
#---Client Commands---
def createBot(token, email=None, password=None, bot=True):
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    client = discord.Client()
    loop.create_task(client.start(token, bot=bot))
    return client
def run():
    asyncio.get_event_loop().run_forever()
class clientCommands():
    def __init__(self, client):
        self.client = client
        asyncio.get_event_loop().create_task(client.wait_until_ready())
    def restart():
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

TOKEN = input("Token > ")
TOKEN = TOKEN.strip('''"''')
BOT = input("Bot T/F > ")
if BOT in ["true", "True", "t", "T"]:
    BOT = True
if BOT in ["false", "False", "f", "F"]:
    BOT = False
bot = clientCommands(client = createBot(TOKEN, bot=BOT))
@bot.client.event
async def on_ready():
    print('ready')
    time.sleep(10)
print("loading...")
run()
