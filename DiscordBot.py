#rewrite

#---Imports---
import asyncio
import discord
import time
import inspect
import subprocess
import os
import sys
#---Settings---
'''Path where setting and saved code files are saved, default is same directory'''
saveFilePath = str(os.path.dirname(os.path.abspath(__file__)))
#---Local Functions---
async def controlPanel(botSelf, conSelf=None, *args, **kwargs):
    global loop
    while loop == True:
        choice = input(" >>> ")
        if choice == "help":
            print("Client Commands\n------------")
            for command in dir(clientCommands):
                if not command.startswith("__"):
                    print(command + str(inspect.signature(getattr(clientCommands, command))).replace("self, ", "").replace("self", ""))
            print("\nLocal Commands\n------------")
            for command in dir(localCommands):
                if not command.startswith("__"):
                    print(command + str(inspect.signature(getattr(localCommands, command))).replace("self, ", "").replace("self", ""))
        elif choice == "end":
            loop = False
        elif choice == "saves":
            for file in os.listdir(saveFilePath):
                if file.startswith("save-"):
                    if file.endswith(".txt"):
                        print(file.split(".")[0].split("save-")[1])
        elif choice.split("(", 1)[0] in dir(localCommands):
            if "(" in choice:
                self = conSelf
                func = getattr(localCommands, choice.split("(",1)[0])
                execPrefix = ""
                if inspect.iscoroutinefunction(func):
                    execPrefix = "await "
                print("Running Command: " + choice.split("(", 1)[0] + "...\n")
                try:
                    exec("async def mainCode(self):\n\ttry:\n\t\t" + execPrefix + "self." + choice.replace("self, ", "").replace("self", "") + "\n\texcept Exception as e:\n\t\tprint('Error: ' + str(e))", globals())
                    await mainCode(self)
                except Exception as e:
                    print(str(e))

        elif choice.split("(", 1)[0] in dir(clientCommands):
            if "(" in choice:
                self = botSelf
                func = getattr(clientCommands, choice.split("(",1)[0])
                execPrefix = ""
                if inspect.iscoroutinefunction(func):
                    execPrefix = "await "
                print("Running Command: " + choice.split("(", 1)[0] + "...\n")
                exec("async def mainCode(self):\n\ttry:\n\t\t" + execPrefix + "self." + choice.replace("self, ", "").replace("self", "") + "\n\texcept Exception as e:\n\t\tprint('Error: ' + str(e))", globals())
                await mainCode(self)
        else:
            exec("async def mainCode():\n\ttry:\n\t\t" + choice + "\n\texcept Exception as e:\n\t\tprint('Error: ' + str(e))", globals())
            await mainCode()
#---Local Commands---
class localCommands():
    def __init__(self, _file_):
        self._file_ = _file_
    def UpdateSetting(self, variable, value):
        '''
        Test description
        '''
        updated = False
        counter = 0
        if os.path.isfile(self._file_+"/Settings"):
            SettingsList = open(self._file_+"/Settings", "r").read().split("\n")
            for i in SettingsList:
                if i.startswith(variable):
                    SettingsList[counter] = variable + " = "  + value
                    updated = True
                counter += 1
            if not updated:
                SettingsList.append(variable + " = "  + value)
            open(self._file_+"/Settings", "w").write("\n".join(SettingsList))
        else:
            open(self._file_+"/Settings", "w").write(variable + " = "  + value)
    def GetSetting(self, variable, output=False):
        if not os.path.isfile(self._file_+"/Settings"):
            if output == True:
                print("None")
            return None
        for i in open(self._file_+"/Settings", "r").read().split("\n"):
            if i.startswith(variable):
                value = i.split("=")[1]
                if output == True:
                    if value == None:
                        print("None")
                    else:
                        print(value)
                if value == "True":
                    value = True
                if value == "False":
                    value = False
                return value
        if output == True:
            print("None")
        return None
    def createSave(self, saveName, code=None):
        if code != None:
            open(self._file_+"/save-"+saveName+".txt", "w").write(code)
        else:
            open(self._file_+"/save-"+saveName+".txt", "w").write("")
    def openSave(self, saveName):
        os.system(self._file_+"/save-"+saveName+".txt")
    async def loadSave(self, saveName):
        counter = 0
        print("Running File: " + saveName + "...\n")
        code = open(self._file_+"/save-"+saveName+".txt", "r").read().split("\n")
        for line in code:
            try:
                func = getattr(clientCommands, line.split("(",1)[0].split(".")[1])
            except Exception:
                try:
                    func = getattr(clientCommands, line.split("(",1)[0])
                    line = "bot." + line
                except Exception:
                    pass
            if "await" not in line:
                if inspect.iscoroutinefunction(func):
                    line = "await " + line
            try:
                func = getattr(localCommands, line.split("(",1)[0].split(".")[1])
            except Exception:
                try:
                    func = getattr(localCommands, line.split("(")[0])
                    line = "con." + line
                except Exception:
                    pass
            if "await" not in line:
                if inspect.iscoroutinefunction(func):
                    line = "await " + line
            code[counter] = "\t\t" + line
            counter += 1
        code = "\n".join(code)
        if self.GetSetting("autoOutput") != False:
            print("async def mainCode():\n\ttry:\n" + code + "\n\texcept Exception as e:\n\t\tprint('Error: ' + str(e))")
        exec("async def mainCode():\n\ttry:\n" + code + "\n\texcept Exception as e:\n\t\tprint('Error: ' + str(e))", globals())
        await mainCode()
#---Client Commands---
class clientCommands():
    def __init__(self, client):
        self.client = client
    async def Cprint(self, variable):
        print(variable)
        try:
            await self.sendMessage(535550762655285271, variable)
        except:
            pass
    async def sendMessage(self, channelID, message):
        channel = self.client.get_channel(int(channelID))
        try:
            await channel.send(message)
        except:
            pass
        if con.GetSetting("autoOutput") != False:
            print("Message sent")
    def autoListen(self, channelID=None):
        global loop
        @self.client.event
        async def on_message(message):
            if message.channel.id == channelID or channelID==None:
                print(message.author.name + " > " + message.content)
        loop = False
bot = clientCommands(discord.Client())
con = localCommands(saveFilePath)
#---Running---
@bot.client.event
async def on_ready():
    global loop
    t1 = time.time()
    await bot.Cprint("\n------")
    await bot.Cprint("Logged Into: " + str(bot.client.user.name))
    await bot.Cprint("Login Time: " + str(round(t1-t0, 1)) + "s")
    await bot.Cprint("------\n")
    loop = True
    while loop == True:
        await controlPanel(bot, conSelf=con)
    @bot.client.event
    async def on_ready():
        pass
#----Live Loop---
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
print("discord.py " + discord.__version__)
if con.GetSetting("autoRunCode") == True:
    mainText = open(_file_+"/Saved_Code", "r").read()
if con.GetSetting("REPL") == True:
    TOKEN = os.environ.get("TOKEN")
    BOT = os.environ.get("BOT")
    if TOKEN == None: TOKEN = input("Token   > ").strip('''"''')
    if BOT == None: BOT = input("Bot T/F > ")
else:
    TOKEN = con.GetSetting("TOKEN")
    BOT = con.GetSetting("BOT")
    if TOKEN == None: TOKEN = input("Token   > ").strip('''"''')
    if BOT == None: BOT = input("Bot T/F > ")
if BOT in ["false", "False", "f", "F"]: BOT = False
else: BOT = True

print("loading...")
t0 = time.time()
bot.client.run(TOKEN, bot=BOT)
