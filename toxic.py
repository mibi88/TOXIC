import discord

TOKEN = "token"

intents = discord.Intents.default()  
intents.message_content = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print("event")
    if message.author == client.user:
        return
    with open("liste_francais_sans_accents.txt", "r") as file:
        data = file.read()
    data = data.split('\n')
    s = message.content
    o = ""
    for w in s.split(' '):
        f = 0
        for i in data:
            if len(i)>len(w):
                if i[0:len(w)] == w.strip().lower():
                    o += i + ' '
                    f = 1
                    break
        if not f: o += w + ' '
    await message.channel.send(o)

client.run(TOKEN)
