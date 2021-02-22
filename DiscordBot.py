#rewrite
#---Imports---
from __future__ import unicode_literals, print_function
OGprint = print
OGinput = input
from prompt_toolkit import print_formatted_text as ANSIprint, ANSI
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
class ansi():
    def __init__(self):
        pass
    _PY2 = sys.version_info[0] == 2
    string_types = basestring if _PY2 else str
    css_colors = {
        'aliceblue':      (240, 248, 255),
        'antiquewhite':   (250, 235, 215),
        'aqua':           (0, 255, 255),
        'aquamarine':     (127, 255, 212),
        'azure':          (240, 255, 255),
        'beige':          (245, 245, 220),
        'bisque':         (255, 228, 196),
        'black':          (0, 0, 0),
        'blanchedalmond': (255, 235, 205),
        'blue':           (0, 0, 255),
        'blueviolet':     (138, 43, 226),
        'brown':          (165, 42, 42),
        'burlywood':      (222, 184, 135),
        'cadetblue':      (95, 158, 160),
        'chartreuse':     (127, 255, 0),
        'chocolate':      (210, 105, 30),
        'coral':          (255, 127, 80),
        'cornflowerblue': (100, 149, 237),
        'cornsilk':       (255, 248, 220),
        'crimson':        (220, 20, 60),
        'cyan':           (0, 255, 255),
        'darkblue':       (0, 0, 139),
        'darkcyan':       (0, 139, 139),
        'darkgoldenrod':  (184, 134, 11),
        'darkgray':       (169, 169, 169),
        'darkgreen':      (0, 100, 0),
        'darkgrey':       (169, 169, 169),
        'darkkhaki':      (189, 183, 107),
        'darkmagenta':    (139, 0, 139),
        'darkolivegreen': (85, 107, 47),
        'darkorange':     (255, 140, 0),
        'darkorchid':     (153, 50, 204),
        'darkred':        (139, 0, 0),
        'darksalmon':     (233, 150, 122),
        'darkseagreen':   (143, 188, 143),
        'darkslateblue':  (72, 61, 139),
        'darkslategray':  (47, 79, 79),
        'darkslategrey':  (47, 79, 79),
        'darkturquoise':  (0, 206, 209),
        'darkviolet':     (148, 0, 211),
        'deeppink':       (255, 20, 147),
        'deepskyblue':    (0, 191, 255),
        'dimgray':        (105, 105, 105),
        'dimgrey':        (105, 105, 105),
        'dodgerblue':     (30, 144, 255),
        'firebrick':      (178, 34, 34),
        'floralwhite':    (255, 250, 240),
        'forestgreen':    (34, 139, 34),
        'fuchsia':        (255, 0, 255),
        'gainsboro':      (220, 220, 220),
        'ghostwhite':     (248, 248, 255),
        'gold':           (255, 215, 0),
        'goldenrod':      (218, 165, 32),
        'gray':           (128, 128, 128),
        'green':          (0, 128, 0),
        'greenyellow':    (173, 255, 47),
        'grey':           (128, 128, 128),
        'honeydew':       (240, 255, 240),
        'hotpink':        (255, 105, 180),
        'indianred':      (205, 92, 92),
        'indigo':         (75, 0, 130),
        'ivory':          (255, 255, 240),
        'khaki':          (240, 230, 140),
        'lavender':       (230, 230, 250),
        'lavenderblush':  (255, 240, 245),
        'lawngreen':      (124, 252, 0),
        'lemonchiffon':   (255, 250, 205),
        'lightblue':      (173, 216, 230),
        'lightcoral':     (240, 128, 128),
        'lightcyan':      (224, 255, 255),
        'lightgoldenrodyellow': (250, 250, 210),
        'lightgray':      (211, 211, 211),
        'lightgreen':     (144, 238, 144),
        'lightgrey':      (211, 211, 211),
        'lightpink':      (255, 182, 193),
        'lightsalmon':    (255, 160, 122),
        'lightseagreen':  (32, 178, 170),
        'lightskyblue':   (135, 206, 250),
        'lightslategray': (119, 136, 153),
        'lightslategrey': (119, 136, 153),
        'lightsteelblue': (176, 196, 222),
        'lightyellow':    (255, 255, 224),
        'lime':           (0, 255, 0),
        'limegreen':      (50, 205, 50),
        'linen':          (250, 240, 230),
        'magenta':        (255, 0, 255),
        'maroon':         (128, 0, 0),
        'mediumaquamarine': (102, 205, 170),
        'mediumblue':     (0, 0, 205),
        'mediumorchid':   (186, 85, 211),
        'mediumpurple':   (147, 112, 219),
        'mediumseagreen': (60, 179, 113),
        'mediumslateblue': (123, 104, 238),
        'mediumspringgreen': (0, 250, 154),
        'mediumturquoise': (72, 209, 204),
        'mediumvioletred': (199, 21, 133),
        'midnightblue':   (25, 25, 112),
        'mintcream':      (245, 255, 250),
        'mistyrose':      (255, 228, 225),
        'moccasin':       (255, 228, 181),
        'navajowhite':    (255, 222, 173),
        'navy':           (0, 0, 128),
        'oldlace':        (253, 245, 230),
        'olive':          (128, 128, 0),
        'olivedrab':      (107, 142, 35),
        'orange':         (255, 165, 0),
        'orangered':      (255, 69, 0),
        'orchid':         (218, 112, 214),
        'palegoldenrod':  (238, 232, 170),
        'palegreen':      (152, 251, 152),
        'paleturquoise':  (175, 238, 238),
        'palevioletred':  (219, 112, 147),
        'papayawhip':     (255, 239, 213),
        'peachpuff':      (255, 218, 185),
        'peru':           (205, 133, 63),
        'pink':           (255, 192, 203),
        'plum':           (221, 160, 221),
        'powderblue':     (176, 224, 230),
        'purple':         (128, 0, 128),
        'rebeccapurple':  (102, 51, 153),
        'red':            (255, 0, 0),
        'rosybrown':      (188, 143, 143),
        'royalblue':      (65, 105, 225),
        'saddlebrown':    (139, 69, 19),
        'salmon':         (250, 128, 114),
        'sandybrown':     (244, 164, 96),
        'seagreen':       (46, 139, 87),
        'seashell':       (255, 245, 238),
        'sienna':         (160, 82, 45),
        'silver':         (192, 192, 192),
        'skyblue':        (135, 206, 235),
        'slateblue':      (106, 90, 205),
        'slategray':      (112, 128, 144),
        'slategrey':      (112, 128, 144),
        'snow':           (255, 250, 250),
        'springgreen':    (0, 255, 127),
        'steelblue':      (70, 130, 180),
        'tan':            (210, 180, 140),
        'teal':           (0, 128, 128),
        'thistle':        (216, 191, 216),
        'tomato':         (255, 99, 71),
        'turquoise':      (64, 224, 208),
        'violet':         (238, 130, 238),
        'wheat':          (245, 222, 179),
        'white':          (255, 255, 255),
        'whitesmoke':     (245, 245, 245),
        'yellow':         (255, 255, 0),
        'yellowgreen':    (154, 205, 50)
    }
    def parse_rgb(self, s):
        if not isinstance(s, self.string_types):
            raise ValueError("Could not parse color '{0}'".format(s))
        s = s.strip().replace(' ', '').lower()
        # simple lookup
        rgb = self.css_colors.get(s)
        if rgb is not None:
            return rgb

        # 6-digit hex
        match = re.match('#([a-f0-9]{6})$', s)
        if match:
            core = match.group(1)
            return tuple(int(core[i:i+2], 16) for i in range(0, 6, 2))

        # 3-digit hex
        match = re.match('#([a-f0-9]{3})$', s)
        if match:
            return tuple(int(c*2, 16) for c in match.group(1))

        # rgb(x,y,z)
        match = re.match(r'rgb\((\d+,\d+,\d+)\)', s)
        if match:
            return tuple(int(v) for v in match.group(1).split(','))

        raise ValueError("Could not parse color '{0}'".format(s))
    # Copyright (c) 2012 Giorgos Verigakis <verigak@gmail.com>
    #
    # Permission to use, copy, modify, and distribute this software for any
    # purpose with or without fee is hereby granted, provided that the above
    # copyright notice and this permission notice appear in all copies.
    _PY2 = sys.version_info[0] == 2
    string_types = basestring if _PY2 else str
    from functools import partial

    # ANSI color names. There is also a "default"
    COLORS = ('black', 'red', 'green', 'yellow', 'blue',
              'magenta', 'cyan', 'white')

    # ANSI style names
    STYLES = ('none', 'bold', 'faint', 'italic', 'underline', 'blink',
              'blink2', 'negative', 'concealed', 'crossed')


    def is_string(self, obj):
        """
        Is the given object a string?
        """
        return isinstance(obj, self.string_types)


    def _join(self, *values):
        """
        Join a series of values with semicolons. The values
        are either integers or strings, so stringify each for
        good measure. Worth breaking out as its own function
        because semicolon-joined lists are core to ANSI coding.
        """
        return ';'.join(str(v) for v in values)


    def _color_code(self, spec, base):
        """
        Workhorse of encoding a color. Give preference to named colors from
        ANSI, then to specific numeric or tuple specs. If those don't work,
        try looking up look CSS color names or parsing CSS hex and rgb color
        specifications.

        :param str|int|tuple|list spec: Unparsed color specification
        :param int base: Either 30 or 40, signifying the base value
            for color encoding (foreground and background respectively).
            Low values are added directly to the base. Higher values use `
            base + 8` (i.e. 38 or 48) then extended codes.
        :returns: Discovered ANSI color encoding.
        :rtype: str
        :raises: ValueError if cannot parse the color spec.
        """
        if self.is_string(spec):
            spec = spec.strip().lower()

        if spec == 'default':
            return self._join(base + 9)
        elif spec in self.COLORS:
            return self._join(base + self.COLORS.index(spec))
        elif isinstance(spec, int) and 0 <= spec <= 255:
            return self._join(base + 8, 5, spec)
        elif isinstance(spec, (tuple, list)):
            return self._join(base + 8, 2, self._join(*spec))
        else:
            rgb = self.parse_rgb(spec)
            # parse_rgb raises ValueError if cannot parse spec
            return self._join(base + 8, 2, self._join(*rgb))


    def color(self, s, fg=None, bg=None, style=None):
        """
        Add ANSI colors and styles to a string.

        :param str s: String to format.
        :param str|int|tuple fg: Foreground color specification.
        :param str|int|tuple bg: Background color specification.
        :param str: Style names, separated by '+'
        :returns: Formatted string.
        :rtype: str (or unicode in Python 2, if s is unicode)
        """
        codes = []

        if fg:
            codes.append(self._color_code(fg, 30))
        if bg:
            codes.append(self._color_code(bg, 40))
        if style:
            for style_part in style.split('+'):
                if style_part in STYLES:
                    codes.append(STYLES.index(style_part))
                else:
                    raise ValueError('Invalid style "%s"' % style_part)

        if codes:
            template = '\x1b[{0}m{1}\x1b[0m'
            if self._PY2 and isinstance(s, unicode):
                # Take care in PY2 to return str if string is given, and
                # unicode if unicode is given. It's a pain, but given PY2's
                # fragility with Unicode characters and encodings, important
                # to avoid any disruptions that might trigger downstream errors.
                template = unicode(template)
            return template.format(self._join(*codes), s)
        else:
            return s


    def strip_color(self, s):
        """
        Remove ANSI color/style sequences from a string. The set of all
        possibly ANSI sequences is large, so does not try to strip every
        possible one. But does strip some outliers seen not just in text
        generated by this module, but by other ANSI colorizers in the wild.
        Those include `\x1b[K` (aka EL or erase to end of line) and `\x1b[m`
        a terse version of the more common `\x1b[0m`.
        """
        return re.sub('\x1b\\[(K|.*?m)', '', s)


    def ansilen(self, s):
        """
        Given a string with embedded ANSI codes, what would its
        length be without those codes?
        """
        return len(strip_color(s))


    # Foreground color shortcuts
    black = partial(color, fg='black')
    red = partial(color, fg='red')
    green = partial(color, fg='green')
    yellow = partial(color, fg='yellow')
    blue = partial(color, fg='blue')
    magenta = partial(color, fg='magenta')
    cyan = partial(color, fg='cyan')
    white = partial(color, fg='white')

    # Style shortcuts
    bold = partial(color, style='bold')
    none = partial(color, style='none')
    faint = partial(color, style='faint')
    italic = partial(color, style='italic')
    underline = partial(color, style='underline')
    blink = partial(color, style='blink')
    blink2 = partial(color, style='blink2')
    negative = partial(color, style='negative')
    concealed = partial(color, style='concealed')
    crossed = partial(color, style='crossed')
ansi = ansi()

#---Variables---
'''Fundamental settings for the rest the code'''
VERSION = "3.2"
if os.path.isdir(r"C:\Users\User\Documents\Python_Coding\DiscordBot_Codes"): saveFilePath = r"C:\Users\User\Documents\Python_Coding\DiscordBot_Codes" #file where everything is saved
else: saveFilePath = None #file where everything is saved
BOT = True
TOKEN = None
consoleCommands = [
    ["create save", "createSave"],
    ["delete save", "deleteSave"],
    ["remove save", "deleteSave"],
    ["open save", "openSave"],
    ["cmd save", "cmdSave"],
    ["cmd run", "cmdSave"],
    ["cmd load", "cmdSave"],
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
            for j in choice.replace("(", " ").replace(")", " ").replace(":", " ").split(" "):
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
        print("\nRunning Command...\n")
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
            for file in os.listdir(con._file_):
                if file.startswith("save-"):
                    if file.endswith(".txt") or file.endswith(".py"):
                        print(file.split("save-")[1])
        else:
            if findCommand(choice, localCommands):
                if conSelf == None:
                    print("Local commands turned off", error)
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
                    print("Not signed into Discord client", error)
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
                print("async def mainCode(self1, self2):\n\ttry:\n\t\t" + choice + "\n\texcept Exception as e:\n\t\tprint('ERROR: ' + str(e), error)\n\tglobals().update(locals())")
            exec("async def mainCode(self1, self2):\n\ttry:\n\t\t" + choice + "\n\texcept Exception as e:\n\t\tprint('ERROR: ' + str(e), error)\n\tglobals().update(locals())", globals())
            await mainCode(conSelf, botSelf)
        except Exception as e:
            print("ERROR: " + str(e), error)
    if not con.getSetting("terminal"):
        print("_________________________________________________________________________________________________", greyText)
    else:
        print("------------", greyText)
def color(text, foregroundRGBcolor=[255,255,255], backgroundRGBcolor=[0,0,0]):
    if not con.getSetting("terminal"):
        if isinstance(foregroundRGBcolor, str):
            print(text, colorCode=foregroundRGBcolor)
        else:
            ANSIprint(ANSI(ansi.color(text, fg=foregroundRGBcolor, bg=backgroundRGBcolor)), end='')
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
        if not saveName.endswith(".txt") and not saveName.endswith(".py"): os.remove(self._file_+"/save-"+saveName+".txt")
        else: os.remove(self._file_+"/save-"+saveName)
    def openSave(self, saveName):
        textEditor = self.getSetting("textEditor")
        if textEditor == None: textEditor = ""
        else: textEditor += " "
        print("Opening File: " + saveName + "...\n")
        if saveName.endswith(".py") or saveName.endswith(".txt"):
            os.system(textEditor + self._file_+"/save-"+saveName)
        else:
            os.system(textEditor + self._file_+"/save-"+saveName+".txt")
    def cmdSave(self, saveName):
            print("Running File: " + saveName + "...\n")
            if saveName.endswith(".txt"):
                self.createSave(saveName + ".py", open(self._file_+"\save-"+saveName, "r").read())
                os.system(self._file_+"/save-"+saveName+".py")
                self.deleteSave(saveName + ".py")
            if saveName.endswith(".py"):
                os.system(self._file_+"/save-"+saveName)
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
if con.getSetting("terminal"):
    def print(string="", colorCode=None, end="\n"):
        if colorCode != None:
            color(string+end, colorCode)
        else:
            OGprint(string)
    input = OGinput
    error = [255, 0, 0]
    grayText = [200, 200, 200]
@bot.client.event
async def on_ready():
    global loop, loadLoop, submitCommand
    t1 = time.time()
    if not con.getSetting("terminal"):
        loadLoop = True
        loading.join()
    await bot.Cprint("------")
    await bot.Cprint("Logged Into: " + str(bot.client.user.name))
    await bot.Cprint("Login Time: " + str(round(t1-t0, 1)) + "s")
    await bot.Cprint("------")
    if con.getSetting("autoRunFile") not in (None, False, True):
        await con.loadSave(con.getSetting("autoRunFile"))
    if con.getSetting("autoRunFile") == True:
        await con.loadSave("Saved_Code")
    if con.getSetting("autoRunCommand") != None:
        await controlPanel(bot, con, con.getSetting("autoRunCommand"))

    loop = True
    while loop == True:
        if con.getSetting("terminal"):
            submitCommand = "input"
        else:
            time.sleep(1)
        if submitCommand != None:
            await controlPanel(bot, con, inputVar=submitCommand)
            submitCommand = None
    print("END OF CONTROL PANEL\n")
#    async def on_ready():
#        pass
#----Live Loop---
color('''   _____________               ___________'''+"   "+'''
  /   ________   \            /   _______  \\'''+"     "+"\n"+"  |  |", color1, bcolor1)
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
color("  Viper " + VERSION, color2, bcolor1)
color("  \ \ \ \ \ \ \________/", color1, bcolor1)
color("  ", color1, bcolor1)
print("\n")
def login(TOKEN=None, BOT=None, fail=False):
    global t0, loading, loadLoop
    if con.getSetting("signin") == False:
        return
    if con.getSetting("REPL") == True:
        TOKEN = os.environ.get("TOKEN")
        BOT = os.environ.get("BOT")
    elif TOKEN == "" or TOKEN == None:
        TOKEN = con.getSetting("TOKEN")
        BOT = con.getSetting("BOT")
    if not con.getSetting("terminal"):
        if BOT == None:
            BOT = BOT_BUTTON_PRESSED
    if TOKEN == None: TOKEN = input("Token   > ")
    if BOT == None: BOT = input("Bot T/F > ")
    if BOT in ["false", "False", "f", "F", False]: BOT = False
    else: BOT = True
    TOKEN = TOKEN.strip('''"''')
    if TOKEN == "none" or TOKEN == "None":
        async def runLocal():
            global submitCommand
            loop = True
            while loop == True:
                if con.getSetting("terminal"):
                    submitCommand = "input"
                else:
                    time.sleep(1)
                if submitCommand != None:
                    await controlPanel(None, con, inputVar=submitCommand)
                    submitCommand = None
        asyncio.run(runLocal())
    else:
        if not con.getSetting("terminal"):
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
            if not con.getSetting("terminal"):
                loadLoop = True
            time.sleep(0.25)
            print("Login Unsuccessful")
        print("END")

def loginThread(TOKEN=None, BOT=None):
    login(TOKEN, BOT)
    loadLoop=True
if not con.getSetting("terminal"):
    size = 100
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
        HIDE_BUTTON = sg.Button("Hide", size=(size+74,1), pad=(5,0), font="Courier 5")
        LOGO = sg.Text(logo, font=('Courier', 8), justification="center", size=(size,10), text_color='#e66363')
        controlPanelLayout = [
                    [sg.Text('Authorization Token', font="Ariel 11", justification="center"), sg.Input(size=(size-36, 1), key='-TOKEN-'), sg.Button("Login"), BOT_BUTTON],
                    [HIDE_BUTTON],
                    [sg.Multiline(size=(size-3, 30), key=OUTPUT, autoscroll=True, pad=(5, 0))],
                    [sg.Input(size=(size, 1), key="IN"), sg.Button('Submit', visible=False, bind_return_key=True)] ]
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
        HIDE_BUTTON = sg.Button("Hide", size=(size+74,1), pad=(5,0), font=("Courier", 5))
        layout = [  [HIDE_BUTTON],
                    [sg.Multiline(size=(size-3, 30), key=OUTPUT, autoscroll=True, pad=(5, 0))],
                    [sg.Input(size=(size, 1), key="IN"), sg.Button('Submit', visible=False, bind_return_key=True)] ]
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
    HIDE_BUTTON_PRESSED = False
    LOGIN_BUTTON_PRESSED = False
    # Event Loop to process "events" and get the "values" of the inputs

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        try:
            if event == 'Test':
                print("hi")
            elif event == 'Login':
                if not LOGIN_BUTTON_PRESSED:
                    threading.Thread(target=loginThread, args=(str(values['-TOKEN-']),), daemon=True).start()
                    LOGIN_BUTTON_PRESSED = True
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
                if not HIDE_BUTTON_PRESSED:
                    OGwindow = window
                    createLayout2()
                    OGwindow.close()
                    HIDE_BUTTON_PRESSED = True
                else:
                    OGwindow = window
                    createLayout1()
                    OGwindow.close()
                    HIDE_BUTTON_PRESSED = False
            else:
                pass
        except Exception as e:
            print(str(e))
    window.close()
else:
    login(TOKEN, BOT)
