#rewrite

#---Imports---
import asyncio
import discord

#---Client Commands---
class clientCommands():
    def _init_:
        self.client = client
        asyncio.get_event_loop().create_task(client.wait_until_ready())
    def createBot(token, email=None, password=None, bot=True):
        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        client = discord.Client()
        loop.create_task(client.start(token, bot=bot))
        return client
    def run():
        asyncio.get_event_loop().run_forever()
    def restart():
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

bot = cleintCommands(self)
TOKEN = input("Token > ")
BOT = input("Bot T/F > ")
if BOT in ["true", "True", "t", "T"]:
    BOT = True
if BOT in ["false", "False", "f", "F"]:
    BOT = False
client = bot.createBot(TOKEN, bot=BOT)
@cleint.event
async def on_ready():
    print('ready')
