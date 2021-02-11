#rewrite
'''
TO-DO LIST
- Get rid of relogin
- Make commands easier to call
- Make settings page, "Tabs" section in cookbook
- Make protogen server to test GUI
'''
#---Imports---
from __future__ import unicode_literals, print_function
OGprint = print
from prompt_toolkit import print_formatted_text as ANSIprint, ANSI
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
import PySimpleGUI as sg
import re
import pytz
#---Variables---
'''Fundamental settings for the rest the code'''
VERSION = "3.1"
saveFilePath = None #file where everything is saved
textEditor = "notepad"
BOT = True
TOKEN = None
consoleCommands = [
    ["create save", "createSave"],
    ["open save", "openSave"],
    ["cmd save", "cmdSave"],
    ["terminal save", "cmdSave"],
    ["run save in terminal", "cmdSave"],
    ["load save in terminal", "cmdSave"],
    ["run save", "loadSave"],
    ["load save", "loadSave"],
    ["rename save", "renameSave"],
    ["update setting", "updateSetting"],
    ["get setting", "getSetting"],
    ]

'''Variables for the rest of code'''
submitCommand = None
submitInput = None
inputMode = False

#Logo colors
color1 = [255,100,100] #snake color RGB
bcolor1 = [30,30,30] #background color RGB
bcolor2 = [50,50,50] #backgorund color RGB
color2 = [255,0,0] #logo color RGB

#General colors
#error = "red"
error = "red"
greyText = "grey"

#All setting
allSettings = '''TOKEN - Discord authorization token to log in
BOT - T/F Bot account?
autoOutput - T/F Prints more information from each command, good for testing
autoRunFile - Automatically runs a save file, open Settings.txt and delete the setting to disable.'''

#---Local Functions---
def print(string="", colorCode=None, end="\n"):
    if colorCode != None:
        sg.cprint(string, text_color=colorCode, end=end)
    else:
        sg.cprint(str(string))
def input(string=""):
    global inputMode, submitInput
    print(string, end="")
    inputMode = True
    while True:
        time.sleep(1)
        if submitInput != None:
            input = submitInput
            submitInput = None
            inputMode = False
            return input
def findCommand(choice, classVar, get=False):
    choice = choice.replace(" ", "").replace("\t", "")
    for i in dir(classVar):
        if not i.startswith("__"):
            for j in choice.replace("(", " ").replace(")", " ").split(" "):
                if i == j:
                    if get:
                        return i
                    else:
                        return True
    return False
def consoleCommand(choice):
    for subList in consoleCommands:
        if choice.startswith(subList[0]):
            realCommand = subList[1]
            textCommand = subList[0]
            arguments = "(" + choice.replace(textCommand+" ", "").replace(" ", ",") + ")"
            return realCommand + arguments
    return choice
async def controlPanel(botSelf=None, conSelf=None, inputVar="input", *args, **kwargs):
    global loop
    if inputVar == "input":
        choice = input("\n >>> ")
    else:
        choice = inputVar
    if "\n" not in choice:
            print("\n >>> ", greyText, "")
            print(choice + "\n")
            print("Running Command...\n")
    choiceList = choice.split("\n")
    finalList = []
    for choice in choiceList:
        OGchoice = choice
        choice = consoleCommand(choice)
        if choice == "":
            pass
        elif choice == "help":
            if botSelf != None:
                print("Client Commands\n------------")
                for command in dir(clientCommands):
                    if not command.startswith("__"):
                        print(command + str(inspect.signature(getattr(clientCommands, command))).replace("self, ", "").replace("self", ""))
            if conSelf != None:
                print("\nLocal Commands\n------------")
                for command in dir(localCommands):
                    if not command.startswith("__"):
                        print(command + str(inspect.signature(getattr(localCommands, command))).replace("self, ", "").replace("self", ""))
            print("\nShort Cuts\n------------")
            print("help - this page\nsaves - shows all saves\nsettings - shows all settings")
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
        elif choice == "saves":
            #if conSelf == None:
            #    color("Local commands turned off", error)
            for file in os.listdir(saveFilePath):
                if file.startswith("save-"):
                    if file.endswith(".txt") or file.endswith(".py"):
                        print(file.split("save-")[1])
        else:
            if findCommand(choice, localCommands):
                if conSelf == None:
                    color("Local commands turned off", error)
                    return
                if "(" in choice:
                    self = conSelf
                    counter=0
                    for i in range(sum(choice.count(x) for x in ("(", " "))):
                        text = choice.replace("(", " ").split(" ")[counter].replace(")", "").replace('''"''', "")
                        counter += 1
                        command = findCommand(text, localCommands, True)
                        try:
                            func = getattr(localCommands, command)
                            execPrefix = ""
                            if inspect.iscoroutinefunction(func):
                                if ("await " + command) not in choice:
                                    choice = choice.replace(command, "await " + command)
                            if ("self1." + command) not in choice:
                                choice = choice.replace(command, "self1." + command)
                        except Exception as e:
                            pass
            if findCommand(choice, clientCommands):
                if botSelf == None:
                    color("Not signed into Discord client", error)
                    return
                if "(" in choice:
                    self = botSelf
                    counter=0
                    for i in range(sum(choice.count(x) for x in ("(", " "))):
                        text = choice.replace("(", " ").split(" ")[counter].replace(")", "").replace('''"''', "")
                        counter += 1
                        command = findCommand(text, clientCommands, True)
                        try:
                            func = getattr(clientCommands, command)
                            execPrefix = ""
                            if inspect.iscoroutinefunction(func):
                                if ("await " + command) not in choice:
                                    choice = choice.replace(command, "await " + command)
                            if ("self2." + command) not in choice:
                                choice = choice.replace(command, "self2." + command)
                        except Exception as e:
                            pass
            finalList.append(choice)
    choice = "\n".join(finalList)
    if choice not in ["", " ", "\n"]:
        try:
            if con.getSetting("autoOutput"):
                print("async def mainCode(self1, self2):\n\ttry:\n\t\t" + choice + "\n\texcept Exception as e:\n\t\tcolor('Error: ' + str(e), error)\n\tglobals().update(locals())")
            exec("async def mainCode(self1, self2):\n\ttry:\n\t\t" + choice + "\n\texcept Exception as e:\n\t\tcolor('Error: ' + str(e), error)\n\tglobals().update(locals())", globals())
            await mainCode(conSelf, botSelf)
        except Exception as e:
            color("ERROR: " + str(e), error)
    color("_________________________________________________________________________________________________", greyText)
def color(text, foregroundRGBcolor=[255,255,255], backgroundRGBcolor=[0,0,0]):
    if isinstance(foregroundRGBcolor, str):
        print(text, colorCode=foregroundRGBcolor)
    else:
        ANSIprint(ANSI(ansi.color(text, fg=foregroundRGBcolor, bg=backgroundRGBcolor)), end='')

#---Local Commands---
class localCommands():
    def __init__(self, _file_, *args, **kwargs):
        if _file_ == None:
            _file_ = str(os.path.dirname(os.path.abspath(__file__)))
        self._file_ = _file_
    def updateSetting(self, variable, value):
        value = str(value)
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
                value = setting.split("=")[1].replace(" ", "")
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
        if saveName.endswith(".py") or saveName.endswith(".txt"):
            file = open(self._file_+"/save-"+saveName, "w")
        else:
            file = open(self._file_+"/save-"+saveName+".txt", "w")
        if code != None:
            file.write(code)
        else:
            file.write("")
    def deleteSave(self, saveName):
        os.remove(self._file_+"\save-"+saveName)
    def openSave(self, saveName):
        textEditor = getSetting("textEditor")
        if textEditor == None: textEditor = ""
        else: textEditor += " "
        print("Opening File: " + saveName + "...\n")
        if saveName.endswith(".py") or saveName.endswith(".txt"):
            os.system(textEditor + self._file_+"\save-"+saveName)
        else:
            os.system(textEditor + self._file_+"\save-"+saveName+".txt")
    def cmdSave(self, saveName):
            print("Running File: " + saveName + "...\n")
            if saveName.endswith(".txt"):
                self.createSave(saveName + ".py", open(self._file_+"\save-"+saveName, "r").read()))
            if saveName.endswith(".py"):
                os.system(self._file_+"\save-"+saveName)
            else:
                os.system(self._file_+"\save-"+saveName+".py")
            self.deleteSave(saveName + ".py")
    async def loadSave(self, saveName):
        global loop
        counter = 0
        func = None
        tab = True
        print("Running File: " + saveName + "...\n")
        if saveName.endswith(".py") or saveName.endswith(".txt"):
            file = open(self._file_+"/save-"+saveName, "r")
        else:
            file = open(self._file_+"/save-"+saveName+".txt", "r")
        code = file.read().split("\n")
        if "" in code: code.remove("")
        for line in code:
            list = re.split("\t|    ", line)
            if tab == True:
                code[counter] = "\t\t" + line
            if "('''" in line:
                tab = False
            if "''')" in line:
                tab = True
            counter += 1
        code.insert(0, "client=bot.client")
        code = "\n".join(code)
        if "@client" in code or "@bot.client" in code:
            loop = False
        if code == "\t\t":
            code += "pass"
        await controlPanel(bot, con, code)
    def renameSave(self, saveName, newSaveName):
        if saveName.endswith(".py") or saveName.endswith(".txt"):
            file = self._file_+"/save-"+saveName
        else:
            file = self._file_+"/save-"+saveName+".txt"
        if newSaveName.endswith(".py") or newSaveName.endswith(".txt"):
            newSaveName = self._file_+"/save-"+newSaveName
        else:
            newSaveName = self._file_+"/save-"+newSaveName+".txt"
        os.rename(file, newSaveName)
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
        loop = False
        @self.client.event
        async def on_message(message):
            if message.channel.id == channelID or channelID==None:
                print(message.author.name + " > " + message.content)
#---Running---
bot = clientCommands(discord.Client())
con = localCommands(saveFilePath)
@bot.client.event
async def on_ready():
    global loop, loadLoop, submitCommand
    t1 = time.time()
    loadLoop = True
    loading.join()
    await bot.Cprint("------")
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
            time.sleep(1)
            if submitCommand != None:
                await controlPanel(bot, con, inputVar=submitCommand)
                submitCommand = None
    print("END OF CONTROL PANEL\n")
#    async def on_ready():
#        pass
#----Live Loop---
#color('''    _____________               ___________'''+"   "+'''
#   /   ________   \            /   _____   \\'''+"     "+'''
#color("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄", color2, bcolor2)
#color('''|  |'''+"   "+'''
#  |  |''', color1, bcolor1)
#color("█▄─▄▄▀█▄─▄█─▄▄▄▄█─▄▄▄─█▄─▄▄─█▄─█─▄", color2, bcolor2)
#olor('''|  |'''+"       "+'''
# (o  o)''', color1, bcolor1)
#color("█─██─██─██▄▄▄▄─█─███▀██─▄▄▄██▄─▄█", color2, bcolor2)
#color('''|  |'''+"  "+'''
#  \__/''', color1, bcolor1)
#color("▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▀▀▄▄▄▀", color2, bcolor2)
#color('''|  |'''+"      "+'''
#   |              \____________/_______/  /'''+"   "+'''
#   ^   ''', color1, bcolor1)
#color("  Viper 2.0", color2, bcolor1)
#color("  \ \ \ \ \ \ \________/", color1, bcolor1)
#color("  ", color1, bcolor1)
print("\n")
def login(TOKEN=None, BOT=None, fail=False):
    global t0, loading, loadLoop
    if con.getSetting("signin") == False:
        return
    if con.getSetting("REPL") == True:
        TOKEN = os.environ.get("TOKEN")
        BOT = os.environ.get("BOT")
        if TOKEN == None: TOKEN = input("Token   > ")
        if BOT == None: BOT = input("Bot T/F > ")
    elif TOKEN == "" or TOKEN == None:
        TOKEN = con.getSetting("TOKEN")
        BOT = con.getSetting("BOT")
    if BOT == None:
        BOT = BOT_BUTTON_PRESSED
    if BOT in ["false", "False", "f", "F", False]: BOT = False
    else: BOT = True
    TOKEN = TOKEN.strip('''"''')
    if TOKEN == "none" or TOKEN == "None":
        async def runLocal():
            global submitCommand
            loop = True
            while loop == True:
                time.sleep(1)
                if submitCommand != None:
                    await controlPanel(None, con, inputVar=submitCommand)
                    submitCommand = None
        asyncio.run(runLocal())
    else:
        loadLoop = False
        def load():
            for i in itertools.cycle(['.  ','.. ','...','   ']):
                if loadLoop:
                    break
                #print('Loading'+i, end="")
                window[OUTPUT].update('loading'+i)
                time.sleep(0.25)
                output = str(window[OUTPUT].get()).split("\n")
                del output[-2]
                window[OUTPUT].update("\n".join(output))
        loading = threading.Thread(target=load)
        loading.start()
        t0 = time.time()
        try:
            bot.client.run(TOKEN, bot=BOT)
        except discord.errors.HTTPException and discord.errors.LoginFailure as e:
            loadLoop = True
            time.sleep(0.25)
            print("Login Unsuccessful")
        print("END")

def loginThread(TOKEN=None, BOT=None):
    login(TOKEN, BOT)
    loadLoop=True


width = 100
logo = '''
 _____________               ___________
 /   ________   \            /   _____   \\
 |  /▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄|  |
 |  |█▄─▄▄▀█▄─▄█─▄▄▄▄█─▄▄▄─█▄─▄▄─█▄─█─▄|  |
(o  o)█─██─██─██▄▄▄▄─█─███▀██─▄▄▄██▄─▄█|  |
 \__/▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▀▀▄▄▄▀|  |
  |              \____________/_______/  /
  ^    Viper ''' + VERSION + '''   \ \ \ \ \ \ \________/ ''' + "\n discord.py ver: " + discord.__version__
sg.LOOK_AND_FEEL_TABLE['theme'] = {'BACKGROUND': '#3d3d3d',
                                   'TEXT': 'white',
                                   'INPUT': 'black',
                                   'SCROLL': '#e66363',
                                   'TEXT_INPUT': 'white',
                                   'BUTTON': ('black', '#e66363'),
                                   'PROGRESS': 'black',
                                   'BORDER': 1,
                                   'SLIDER_DEPTH': 0,
                                   'PROGRESS_DEPTH': 0}
sg.theme('theme')
OUTPUT = "-OUTPUT-"+sg.WRITE_ONLY_KEY
def createLayout1():
    global BOT_BUTTON, window
    BOT_BUTTON = sg.Button("BOT=T")
    HIDE_BUTTON = sg.Button("Hide", size=(174,1), pad=(5,0), font=("Courier", 5))
    LOGO = sg.Text(logo, font='Courier 10', justification="center", size=(width-int(width/7),10), text_color='#e66363')
    controlPanelLayout = [
                [sg.Text('Authorization Token', font="Arial 11", justification="center"), sg.Input(size=(width-22-14, 1), key='-TOKEN-'), sg.Button("Login"), BOT_BUTTON],
                [HIDE_BUTTON],
                [sg.Multiline(size=(width-3, 30), key=OUTPUT, reroute_stdout=True, reroute_stderr=True, autoscroll=True, pad=(5, 0))],
                [sg.Input(size=(width, 1), key="IN"), sg.Button('Submit', visible=False, bind_return_key=True)] ]
    settingsLayout = [
    [sg.Text("autoOutput")] ]
    shortcutsLayout = [
    [sg.Text("Run in terminal")]  ]
    layout = [[LOGO], [sg.TabGroup([[sg.Tab("Control Panel", controlPanelLayout), sg.Tab("Shortcuts", shortcutsLayout), sg.Tab("Settings", settingsLayout)]])]]
    window = sg.Window('DiscPy Viper ' + VERSION, layout, finalize=True)
    window['IN'].Widget.config(insertbackground='white')
    window['-TOKEN-'].Widget.config(insertbackground='white')
    sg.cprint_set_output_destination(window, OUTPUT)
    HIDE_BUTTON.update("")
    try:
        x = OGwindow[OUTPUT].get().split("\n")
        for i in range(2): x.pop()
        OGprint("\n".join(x))
    except Exception:
        pass

def createLayout2():
    global window
    HIDE_BUTTON = sg.Button("Hide", size=(174,1), pad=(5,0), font=("Courier", 5))
    layout = [  [HIDE_BUTTON],
                [sg.Multiline(size=(width-3, 30), key=OUTPUT, reroute_stdout=True, reroute_stderr=True, autoscroll=True, pad=(5, 0))],
                [sg.Input(size=(width, 1), key="IN"), sg.Button('Submit', visible=False, bind_return_key=True)] ]
    window = sg.Window('DiscPy Viper ' + VERSION, layout, finalize=True)
    window['IN'].Widget.config(insertbackground='white')
    sg.cprint_set_output_destination(window, OUTPUT)
    HIDE_BUTTON.update("")
    x = OGwindow[OUTPUT].get().split("\n")
    for i in range(2): x.pop()
    OGprint("\n".join(x))

# Create the Window
createLayout1()
BOT_BUTTON_PRESSED = True
HIDE_BUTTON_PRESSED = True
LOGIN_BUTTON_PRESSED = True
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    try:
        if event == 'Test':
            print("hi")
        elif event == 'Login':
            if LOGIN_BUTTON_PRESSED:
                threading.Thread(target=loginThread, args=(str(values['-TOKEN-']),), daemon=True).start()
                LOGIN_BUTTON_PRESSED = False
            #else:
            #    window.close()
            #    os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
        elif event == 'Submit' or event == 'Ok':
            if inputMode:
                submitInput = str(values["IN"])
            else:
                submitCommand = str(values["IN"])
            window["IN"].update("")
        elif event == 'BOT=T':
            if BOT_BUTTON_PRESSED:
                BOT_BUTTON.update("BOT=F")
                BOT_BUTTON_PRESSED = False
            else:
                BOT_BUTTON.update("BOT=T")
                BOT_BUTTON_PRESSED = True
        elif event == "Hide":
            if HIDE_BUTTON_PRESSED:
                OGwindow = window
                createLayout2()
                OGwindow.close()
                HIDE_BUTTON_PRESSED = False
            else:
                OGwindow = window
                createLayout1()
                OGwindow.close()
                HIDE_BUTTON_PRESSED = True
        else:
            pass
    except Exception as e:
        print(str(e))
window.close()
