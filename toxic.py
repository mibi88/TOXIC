import discord
import random
import unicodedata

TOKEN = "token"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    with open("liste_francais_sans_accents.txt", "r") as file:
        data = file.read()
    with open("dict_ang2.txt", "r") as file:
        data += '\n' + file.read()
    data = data.split('\n')
    s = message.content
    o = ""
    for w in s.split(' '):
        w = str(unicodedata.normalize('NFD', w).encode('ascii', 'ignore').decode("utf-8"))
        p = []
        f = 0
        for i in data:
            if len(i)>len(w):
                if i[0:len(w)] == w.strip().lower():
                    p.append(i)
                    f = 1
        if not f: o += w + ' '
        else: o += random.choice(p) + ' '
    await message.channel.send(o)

client.run(TOKEN)
