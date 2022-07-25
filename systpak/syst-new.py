import os
import discord

client = discord.Client()
token = open("TOKEN.txt","r").readline()
id=967120742464499763

async def bios():
    await client.wait_until_ready()
    channel = client.get_channel(id) # replace with channel_id
    while not client.is_closed():
        PATH = './keep_alive.py'
        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            await channel.send('Checking keep_alive.py...OK')
            print("Checking keep_alive.py..OK")
            os.system('clear')
            os.system("python3 kern.py")
            break;
        else:
            await channel.send('Checking keep_alive.py...ERROR')
            print("Checking keep_alive.py...ERROR")
            os.system("curl https://updatepakager.legamer4.repl.co/systpak/keep_alive-new.py > keep_alive.py")
            await channel.send('Downloaded reb.py...100%')
            print("Downloaded reb.py...100%")
            os.system('mv keep_alive-new.py keep_alive.py')
            os.system('clear')
            await channel.send('Rebooting...')
            print("Rebooting...")
            os.system("python3 main.py")
            break;

@client.event
async def on_ready():
  print("hey")

client.loop.create_task(bios())  
client.run(token)