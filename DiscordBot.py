#rewrite

#---Imports---
from __future__ import unicode_literals, print_function
OGprint = print
from prompt_toolkit import print_formatted_text as print, ANSI
import colors as ansi
import asyncio
import discord
import time
import inspect
import subprocess
import os
import sys
import itertools
import threading
import colorama
colorama.init()
#---Variables---
'''Fundamental settings for the rest the code'''

saveFilePath = str(os.path.dirname(os.path.abspath(__file__))) #file where everything is saved

#Logo colors
color1 = [255,100,100] #snake color RGB
bcolor1 = [30,30,30] #background color RGB
bcolor2 = [50,50,50] #backgorund color RGB
color2 = [255,0,0] #logo color RGB

#General colors
error = [255,0,0]

#All setting
allSettings = '''TOKEN - Discord authorization token to log in
BOT - T/F Bot account?
autoOutput - T/F Prints more information from each command, good for testing
autoRunFile - Automatically runs a save file, open Settings.txt and delete the setting to disable.'''

#---Local Functions---
def findCommand(choice, classVar, get=False):
    for i in dir(classVar):
        if not i.startswith("__"):
            for j in choice.split("("):
                if i == j:
                    if get:
                        return j
                    else:
                        return True
    return False
async def controlPanel(botSelf, conSelf=None, inputVar="input", *args, **kwargs):
    global loop
    if inputVar == "input":
        choice = input("\n >>> ")
        print()
    else:
        choice = inputVar
    if choice == "":
        pass
    elif choice == "help":
        print("Client Commands\n------------")
        for command in dir(clientCommands):
            if not command.startswith("__"):
                print(command + str(inspect.signature(getattr(clientCommands, command))).replace("self, ", "").replace("self", ""))
        print("\nLocal Commands\n------------")
        for command in dir(localCommands):
            if not command.startswith("__"):
                print(command + str(inspect.signature(getattr(localCommands, command))).replace("self, ", "").replace("self", ""))
        print("\nShort Cuts\n------------")
        print("help - this page\nsaves - shows all saves\nsettings - shows all settings\nend - ends loop")
    elif choice == "restart":
        os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
    elif choice == "settings":
        print("Used Settings\n------------")
        for setting in open(con._file_+"/Settings", "r").read().split("\n"):
            if not setting.startswith("#"):
                if not setting == "":
                    print(setting.replace("=", " = "))
        print("\nAll Settings\n------------")
        print(allSettings)
    elif choice == "end":
        loop = False
    elif choice == "saves":
        for file in os.listdir(saveFilePath):
            if file.startswith("save-"):
                if file.endswith(".txt"):
                    print(file.split(".")[0].split("save-")[1])
    else:
        if findCommand(choice, localCommands):
            if "(" in choice:
                self = conSelf
                command = findCommand(choice, localCommands, True)
                try:
                    func = getattr(localCommands, command)
                except Exception as e:
                    print(color('Error: ' + str(e), error))
                    return
                execPrefix = ""
                if inspect.iscoroutinefunction(func):
                    choice = choice.replace(command, "await " + command)
                choice = choice.replace(command, "self1." + command)

        if findCommand(choice, clientCommands):
            if "(" in choice:
                self = botSelf
                command = findCommand(choice, clientCommands, True)
                try:
                    func = getattr(clientCommands, command)
                except Exception as e:
                    print(color('Error: ' + str(e), error))
                    return
                if inspect.iscoroutinefunction(func):
                    choice = choice.replace(command, "await " + command)
                choice = choice.replace(command, "self2." + command)
        print("Running Command...\n")
        try:
            if con.getSetting("autoOutput"):
                print("async def mainCode(self1, self2):\n\ttry:\n\t\t" + choice + "\n\texcept Exception as e:\n\t\tprint(color('Error: ' + str(e), error))")
            exec("async def mainCode(self1, self2):\n\ttry:\n\t\t" + choice + "\n\texcept Exception as e:\n\t\tprint(color('Error: ' + str(e), error))", globals())
            await mainCode(conSelf, botSelf)
        except Exception as e:
            print(color("GUI ERROR: " + str(e), error))
def color(text, foregroundRGBcolor=[255,255,255], backgroundRGBcolor=[0,0,0]):
    print(ANSI(ansi.color(text, fg=foregroundRGBcolor, bg=backgroundRGBcolor)), end='')
#---Local Commands---
class localCommands():
    def __init__(self, _file_):
        self._file_ = _file_
    def updateSetting(self, variable, value):
        '''
        Test description
        '''
        updated = False
        counter = 0
        if os.path.isfile(self._file_+"/Settings"):
            SettingsList = open(self._file_+"/Settings", "r").read().split("\n")
            for setting in SettingsList:
                if variable == setting.split("=")[0].replace(" ", ""):
                    SettingsList[counter] = variable + " = "  + value
                    updated = True
                counter += 1
            if not updated:
                SettingsList.append(variable + " = "  + value)
            open(self._file_+"/Settings", "w").write("\n".join(SettingsList))
        else:
            open(self._file_+"/Settings", "w").write(variable + " = "  + value)
    def getSetting(self, variable, output=False):
        if not os.path.isfile(self._file_+"/Settings"):
            if output == True:
                print("None")
            return None
        for setting in open(self._file_+"/Settings", "r").read().split("\n"):
            if variable == setting.split("=")[0].replace(" ", "") or variable == "all":
                value = setting.split("=")[1]
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
        func = None
        tab = True
        print("Running File: " + saveName + "...\n")
        code = open(self._file_+"/save-"+saveName+".txt", "r").read().split("\n")
        if "" in code: code.remove("")
        for line in code:
            try:
                func = getattr(clientCommands, line.split("(",1)[0].split(".")[1])
            except Exception:
                try:
                    func = getattr(clientCommands, line.split("(",1)[0])
                    line = "bot." + line
                except Exception:
                    pass
            if func != None:
                if not line.replace("\t", "").replace(" ", "").startswith("await"):
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
            if func != None:
                if not line.replace("\t", "").replace(" ", "").startswith("await"):
                    if inspect.iscoroutinefunction(func):
                        line = "await " + line
            if tab == True:
                code[counter] = "\t\t" + line
            if "('''" in line:
                tab = False
            if "''')" in line:
                tab = True
            counter += 1
        code = "\n".join(code)
        if code == "\t\t":
            code += "pass"
        if self.getSetting("autoOutput") == True:
            print("async def mainCode():\n\ttry:\n" + code + "\n\texcept Exception as e:\n\t\tprint(color('Error: ' + str(e), error))")
        exec("async def mainCode():\n\ttry:\n" + code + "\n\texcept Exception as e:\n\t\tprint(color('Error: ' + str(e), error))", globals())
        await mainCode()
#---Client Commands---
class clientCommands():
    def __init__(self, client):
        self.client = client
    async def commandCenter(self, prefix = "cc:"):
        global loop
        @self.client.event
        async def on_message(message):
            if int(message.channel.id) == 562821889685323776:
                text = str(message.content)
                if "cc:" in text:
                    text = text.split("\n")
                    text[0] = text[0].replace("cc:", "")
                    for line in text:
                        await controlPanel(self, con, line)
        loop = False
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
        if con.getSetting("autoOutput") == True:
            print("Message sent")
    def autoListen(self, channelID=None):
        global loop
        @self.client.event
        async def on_message(message):
            if message.channel.id == channelID or channelID==None:
                print(message.author.name + " > " + message.content)
        loop = False
#---Running---
bot = clientCommands(discord.Client())
con = localCommands(saveFilePath)
@bot.client.event
async def on_ready():
    global loop, loadLoop
    t1 = time.time()
    loadLoop = True
    await bot.Cprint("\n------")
    await bot.Cprint("Logged Into: " + str(bot.client.user.name))
    await bot.Cprint("Login Time: " + str(round(t1-t0, 1)) + "s")
    await bot.Cprint("------")
    if con.getSetting("autoRunFile") not in (None, False, True):
        await con.loadSave(con.getSetting("autoRunFile"))
    elif con.getSetting("autoRunFile") == True:
        await con.loadSave("Saved_Code")
    elif con.getSetting("autoRunCommand") != None:
        await controlPanel(bot, con, con.getSetting("autoRunCommand"))
    else:
        loop = True
        while loop == True:
            await controlPanel(bot, con)
    @bot.client.event
    async def on_ready():
        pass
#----Live Loop---

color('''    _____________               ___________'''+"   "+'''
   /   ________   \            /   _____   \\'''+"     "+'''
  |  /''', color1, bcolor1)
color("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄", color2, bcolor2)
color('''|  |'''+"   "+'''
  |  |''', color1, bcolor1)
color("█▄─▄▄▀█▄─▄█─▄▄▄▄█─▄▄▄─█▄─▄▄─█▄─█─▄", color2, bcolor2)
color('''|  |'''+"       "+'''
 (o  o)''', color1, bcolor1)
color("█─██─██─██▄▄▄▄─█─███▀██─▄▄▄██▄─▄█", color2, bcolor2)
color('''|  |'''+"  "+'''
  \__/''', color1, bcolor1)
color("▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▀▀▄▄▄▀", color2, bcolor2)
color('''|  |'''+"      "+'''
   |              \____________/_______/  /'''+"   "+'''
   ^   ''', color1, bcolor1)
color("  Viper 2.0", color2, bcolor1)
color("  \ \ \ \ \ \ \________/", color1, bcolor1)
color("  ", color1, bcolor1)
print("\n")
print("discord.py " + discord.__version__)
if con.getSetting("REPL") == True:
    TOKEN = os.environ.get("TOKEN")
    BOT = os.environ.get("BOT")
    if TOKEN == None: TOKEN = input("Token   > ").strip('''"''')
    if BOT == None: BOT = input("Bot T/F > ")
else:
    TOKEN = con.getSetting("TOKEN")
    BOT = con.getSetting("BOT")
    if TOKEN == None: TOKEN = input("Token   > ").strip('''"''')
    if BOT == None: BOT = input("Bot T/F > ")
if BOT in ["false", "False", "f", "F"]: BOT = False
else: BOT = True
loadLoop = False
def load():
    for i in itertools.cycle(['.  ','.. ','...','   ']):
        if loadLoop:
            break
        sys.stdout.write('\rLoading'+i)
        sys.stdout.flush()
        time.sleep(0.25)
loading = threading.Thread(target=load)
loading.start()
t0 = time.time()
bot.client.run(TOKEN, bot=BOT)
