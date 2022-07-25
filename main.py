import os
import discord
client = discord.Client()
token = open("TOKEN.txt","r").readline()
id=967120742464499763

async def my_background_task():
    await client.wait_until_ready()
    channel = client.get_channel(id) # replace with channel_id
    while not client.is_closed():
        PATH2 = './kernel.py'
        await channel.send('-=VKBIOS v0.4=-')
        print("-=VKBIOS v0.4=-")
        await channel.send('testing CD-ROM...')
        if os.path.isfile(PATH2) and os.access(PATH2, os.R_OK):
            await channel.send('testing CD-ROM...DETECTED')
            await channel.send('booting from CD-ROM...')
            print("booting from CD-ROM...")
            os.system('clear')
            os.system('python kernel.py')
            break;
        else:
            await channel.send('testing CD-ROM...ERROR')
            print("testing CD-ROM...ERROR")
            os.system('clear')
            os.system('python3 cdrom.py')
            


@client.event
async def on_ready():
  print("ok")
client.loop.create_task(my_background_task())
client.run(token)