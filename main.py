#!/usr/bin/env python
#bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
#voice = discord.VoiceClient(client, "General")

# viktor = discord.File("/home/barre/Development/Programmering/DiscordBot/viktor.mov", filename =None,spoiler=False)



joydip_nr = 1


# music_channel = client.get_channel("789435195727020034")


def int_to_roman(input):
    """ Convert an integer to a Roman numeral. """

    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)



@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    this_channel = message.channel.id
    music_channel = 789435195727020034
    
    
    
    if this_channel == music_channel:
        print("yo yo korv tilll frulle")
    
    
    moise = [
        'Moise är svart ngl ngl',
        'moise moise moise moise moise moise moise miose mmiose miose moise moise moise mosie moise moise',
        'mowshe',
        discord.File("/home/barre/BarreBot/moise1.jpg", filename =None, spoiler=False),
    ]

    michael = [
        'Michael Sportingsawn',
        'Michael Hawkingson',
        'Michael Rasmusken',
    ]

    barre = [
        'Jag ska inte ljuga, han den där Barre är fan hella sexig.',
        'Tjejer akta er för Barre, han är för söt ngl fr fr',
        'Även fast Barre är lite moisig i skallen är han fortfarande cool ngl',
        'Fr fr visste du att Barre heter Barre Nils Fredrik Svante Åke Blomber',
        discord.File("/home/barre/BarreBot/barre1.jpg", filename =None, spoiler=False),
        discord.File("/home/barre/BarreBot/barre2.jpg", filename =None, spoiler=False),
        ]
    
    babis = [
        discord.File("/home/barre/BarreBot/babis1.png", filename =None,spoiler=False),
        discord.File("/home/barre/BarreBot/babis2.png", filename =None,spoiler=False),
        discord.File("/home/barre/BarreBot/babis3.png", filename =None,spoiler=False),
    ]

    tjejer = [
        'Error 0x4890f3g, teknikare får inte prata om, eller prata med tjejer.',
        'Imagine being a teknikare lmao',
        'Det var typ länge sedan man såg en tjej ngl',
        'https://sv.wikipedia.org/wiki/Poop',
        discord.File("/home/barre/BarreBot/kvinna1.jpg", filename =None, spoiler=False)
    ]

    alex = [
        "Sorry bror, <@221266059506876416> är inte här, han är lite sen.",
        "Alex födelseplats: https://en.wikipedia.org/wiki/Benis"
    ]
    
    benis = [
        discord.File("/home/barre/BarreBot/benis1.png", filename =None, spoiler=False),
        discord.File("/home/barre/BarreBot/benis2.jpg", filename =None, spoiler=False),
    ]

    fysik = [
        discord.File("/home/barre/BarreBot/fysik1.jpg", filename =None, spoiler=False),
        discord.File("/home/barre/BarreBot/fysik2.jpg", filename =None, spoiler=False),
        discord.File("/home/barre/BarreBot/fysik3.jpg", filename =None, spoiler=False),
    ]
    
    
    if "moise" in message.content.lower():
        #voice.connect(True, 1000)
        
        response = random.choice(moise)

        if isinstance(response, str):
            await message.channel.send(response)
        else:
            await message.channel.send(file = response)

    if "michael" in message.content.lower():
        response = random.choice(michael)
        await message.channel.send(response)        

    if "barre" in message.content.lower():
        response = random.choice(barre)

        if isinstance(response, str):
            await message.channel.send(response)
        else:
            print(response.fp.name)
            
            if response.fp.name == "/home/barre/BarreBot/barre2.jpg":
                await message.channel.send(file = response)
                await message.channel.send("Titta vilken stilig pojke, tjejerna flockas.")
            else: 
                await message.channel.send(file = response)               

                
    if "joydip" in message.content.lower():

        global joydip_nr
        
        response = "Joydip Paul " + str(int_to_roman(joydip_nr))
        joydip_nr += 1
        
        await message.channel.send(response)                

    if "viktor" in message.content.lower():
        # response = "viiiiikkkkktooooooooooor *fladdrar med bratten*"
        response = "viktoooooooooooooorrrrrrrrrrr"
        viktor = discord.File("/home/barre/BarreBot/viktor.mov", filename =None,spoiler=True)
        
        await message.channel.send(response)
        await message.channel.send(file = viktor)

    if "babis" in message.content.lower():
        response = "ÅOÅOCheeeeeeeyyy"
        await message.channel.send(response)
        await message.channel.send(file = random.choice(babis))


    if "alex" in message.content.lower():
        response = random.choice(alex)
        await message.channel.send(response)

    if "tjejer" in message.content.lower():
        response = random.choice(tjejer)

        if isinstance(response, str):
            await message.channel.send(response)
        else:
            if response.fp.name == "/home/barre/BarreBot/kvinna1.jpg":
                await message.channel.send("NTI be like")
                await message.channel.send(file = response)
            else:
                await message.channel.send(file = response)


    if "benis" in message.content.lower():
        response = random.choice(benis)
        await message.channel.send(file = response)

    if "fysik" in message.content.lower():
        response = random.choice(fysik)
        await message.channel.send("Fysik be like: ")
        await message.channel.send(file = response)        

# await connect(*, timeout=60.0, reconnect=True, cls=<class 'discord.voice_client.VoiceClient'>  )


#@client.command()
#async def join(ctx):
#    channel = ctx.author.voice.channel
#    await channel.connect()
#@client.command()
#async def leave(ctx):
#    await ctx.voice_client.disconnect()

#voice.

client.run(TOKEN)
