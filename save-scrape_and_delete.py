ServerID = 715882368644153354
UserID = 197177436247425025
MessageLimit = 200000
for guild in client.guilds:
    if str(guild.id) == str(ServerID):
        Cprint("srape.py Start")
        for category in guild.categories:
            color(" > " + category.name, "green")
            for channel in category.channels:
                if str(channel.id) != str(754012746923638805):
                    color(" >> " + channel.name, "green")
                    try:
                        messages = await channel.history(limit=MessageLimit).flatten()
                        for message in messages:
                            if str(message.author.id) == str(UserID):
                                print(message.content)
                                await message.delete()
                    except Exception as e:
                        color(str(e), "red")
Cprint("kitz.py End")
