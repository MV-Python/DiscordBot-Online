class get():
    def printChannels():
        for guild in client.guilds:
            print(guild.name)
            for category in guild.categories:
                print("\t" + category.name)
                for channel in category.channels:
                    print("\t\t" + channel.name)
                    print("\t\t" + str(channel.id), [50, 255, 50])
    def server(serverID=None, serverName=None):
        if serverID == None and serverName == None:
            serverID = input(" Server ID   > ")
            if serverID in ["", " ", "\n", "none", "None", "name", "Name"]:
                serverName = input(" Server Name > ")
        if serverName != None:
            for guild in client.guilds:
                if str(guild.name) == serverName:
                    serverID = guild.id
        for guild in client.guilds:
            if str(guild.id) == str(serverID):
                return guild
    def channel(channelID=None, serverName=None, channelName=None):
        if channelID == None and serverName != None and channelName != None:
            for guild in client.guilds:
                if str(guild.name) == serverName:
                    for channel in guild.channels:
                        if str(channel.name) == channelName:
                            channelID = channel.id
        for guild in client.guilds:
            for channel in guild.channels:
                if str(channel.id) == str(channelID):
                    return channel
class bot():
    async def print(string, *args, **kwargs):
        Cprint(string, **kwargs)
    async def messageSender():
        @client.event
        async def on_message(message):
            print(message)
            Cprint(input(" > "))
